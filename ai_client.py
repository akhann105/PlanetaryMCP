import asyncio
import json
import httpx
import ollama
from mcp import Client

MCP_URL = "http://127.0.0.1:8000/mcp"
REDIS_URL = "http://127.0.0.1:5002"
MODEL = "qwen3:4b"


async def main():

    username = input("Enter your username: ").strip()

    # Connect to the MCP server
    async with Client(MCP_URL) as client:

        result = await client.list_tools()
        tools = []

        # Convert MCP tools into Ollama tools
        for tool in result.tools:
            tools.append({
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": tool.input_schema
                }
            })

        print("\nPlanetary MCP is ready!")
        print("Type exit to quit.\n")

        while True:

            question = input("You: ").strip()

            if question.lower() == "exit":
                break

            if not question:
                continue

            # Record the user's query in Redis
            response = httpx.post(
                f"{REDIS_URL}/query/{username}",
                timeout=30,
                trust_env=False
            )
            response.raise_for_status()

            messages = [
                {
                    "role": "system",
                    "content": (
                        "You are a planetary assistant. "
                        "Use the available tools to answer questions. "
                        "Base your answers on the returned data. "
                        "Do not invent missing information. "
                        "Keep your answers short and clear."
                    )
                },
                {
                    "role": "user",
                    "content": question
                }
            ]

            print("Processing your question...", flush=True)

            # Let Ollama select the appropriate tool
            response = ollama.chat(
                model=MODEL,
                messages=messages,
                tools=tools,
                think=False
            )

            messages.append(response.message)

            # Execute the selected MCP tools
            for call in response.message.tool_calls or []:

                name = call.function.name
                arguments = call.function.arguments

                print(f"Using tool: {name}", flush=True)

                result = await client.call_tool(name, arguments)

                messages.append({
                    "role": "tool",
                    "tool_name": name,
                    "content": json.dumps(
                        result.model_dump(mode="json")
                    )
                })

            # Generate the final answer using the retrieved data
            if response.message.tool_calls:

                print("Generating answer...", flush=True)

                response = ollama.chat(
                    model=MODEL,
                    messages=messages,
                    think=False
                )

            print("\nAI:", response.message.content, "\n")


if __name__ == "__main__":
    asyncio.run(main())