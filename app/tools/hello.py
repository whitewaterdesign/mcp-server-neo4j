from app.mcp import mcp


@mcp.tool()
def greeting(name: str) -> str:
    """
    Greets the caller by name
    :param namne: string - the name of the caller
    :return: string - Returns a greeting
    """
    return f"Hello {name}! Welcome to the Neo4J MCP"