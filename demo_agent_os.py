from agno.os import AgentOS
from agno.os.interfaces.agui import AGUI

from client.agent import movie_agent

# AgentOS manages MCP lifespan
agent_os = AgentOS(
    description="AgentOS with MCP Tools",
    agents=[movie_agent],
    interfaces=[AGUI(agent=movie_agent)]
)

app = agent_os.get_app()

if __name__ == "__main__":
    # Don't use reload=True with MCP tools to avoid lifespan issues
    agent_os.serve(app="demo_agent_os:app", port=8000, reload=True)