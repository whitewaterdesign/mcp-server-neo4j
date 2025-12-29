from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mcp import MCPTools

from client.config import get_config

config = get_config()

async def run_agent():
    # Initialize and connect to the MCP server
    mcp_tools = MCPTools(
        transport="streamable-http",
        url=config.mcp_url
    )
    await mcp_tools.connect()
    print("mcp tools: ", mcp_tools.tools)

    try:
        # Setup and run the agent
        agent = Agent(
            model=OpenAIChat(
                id="gpt-4o-mini",
                api_key=config.openai_api_key,
                temperature=0.0,
            ),
            tools=[mcp_tools],
            debug_mode=True,
            instructions=["You are a simple agent which just answers with responses from tool calls"]
        )
        await agent.aprint_response('Hello, my name is Joe Bloggs', stream=True)
    finally:
        # Always close the connection when done
        await mcp_tools.close()
