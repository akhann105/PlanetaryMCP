# PlanetaryMCP

## Project Overview

PlanetaryMCP is an AI-powered application that allows users to ask questions about planets using natural language. The project combines MongoDB, Redis, Flask, Model Context Protocol (MCP), and Ollama.

MongoDB stores planetary information, while Redis tracks user activity and the total number of queries submitted.

## Technologies Used

- Python
- MongoDB Atlas
- Redis
- Flask
- Model Context Protocol (MCP)
- Ollama (Qwen3 4B)
- HTTPX

## Features

- Retrieve information about planets.
- Search for planets containing specific atmospheric gases.
- Identify planets that have rings.
- Compare planetary temperatures and positions from the Sun.
- Track the total number of queries.
- Track unique users.
- Answer questions through a local AI model.

## Project Files

| File | Description |
|---|---|
| mongo_app.py | MongoDB REST API |
| redis_app.py | Redis REST API |
| mcp_server.py | Connects both APIs to MCP tools |
| ai_client.py | Connects Ollama to the MCP server |
| test_mongo.py | Tests the MongoDB connection |
| test_redis.py | Tests the Redis connection |
| start_servers.ps1 | Starts all three servers |
| requirements.txt | Required Python packages |
| .gitignore | Prevents private files from being uploaded |

## Installation

1. Create and activate a Python virtual environment.
2. Install the packages using `pip install -r requirements.txt`.
3. Create a `.env` file containing your MongoDB connection string as `MONGO_URI`.
4. Start the Redis server.
5. Install Ollama and download the model using `ollama pull qwen3:4b`.

## Running the Application

Start the MongoDB API, Redis API, and MCP server in separate terminals:

- `python mongo_app.py`
- `python redis_app.py`
- `python mcp_server.py`

Then start the AI client:

`python ai_client.py`

Enter a username and begin asking questions.

## Example Questions

- Which planets have rings?
- What planets have H2 in their atmosphere?
- Compare the mean temperatures of all planets.
- How many queries have been recorded?
- How many unique users have used the system?

## Limitations

The current dataset and implementation use planetary positions rather than physical distances from the Sun. Ring information indicates whether a planet has rings rather than the exact number of rings. User tracking counts unique usernames rather than currently connected users.

## Testing

The MongoDB and Redis connections, MCP tools, and Ollama integration were successfully tested. The application successfully retrieved planetary information and user activity statistics through natural language questions.