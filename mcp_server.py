from mcp.server.mcpserver import MCPServer
import httpx

mcp = MCPServer("PlanetaryMCP")

# Flask API addresses
MONGO_URL = "http://127.0.0.1:5001"
REDIS_URL = "http://127.0.0.1:5002"


@mcp.tool()
def get_planets() -> list:
    """Get information about all planets."""
    return httpx.get(f"{MONGO_URL}/planets").json()


@mcp.tool()
def get_atmosphere(gas: str) -> list:
    """Find planets containing a specific atmospheric gas."""
    return httpx.get(f"{MONGO_URL}/atmosphere/{gas}").json()


@mcp.tool()
def get_rings() -> list:
    """Find planets that have rings."""
    return httpx.get(f"{MONGO_URL}/rings").json()


@mcp.tool()
def get_temperature() -> list:
    """Compare planet temperatures and positions from the Sun."""
    return httpx.get(f"{MONGO_URL}/temperature").json()


@mcp.tool()
def get_queries() -> dict:
    """Get the total number of user queries."""
    return httpx.get(f"{REDIS_URL}/queries").json()


@mcp.tool()
def get_users() -> dict:
    """Get the number of unique users."""
    return httpx.get(f"{REDIS_URL}/users").json()


if __name__ == "__main__":
    mcp.run(transport="streamable-http")