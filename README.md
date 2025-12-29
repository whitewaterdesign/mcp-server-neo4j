# MCP Server (Neo4j)

Lightweight MCP (FastMCP) server that integrates with a Neo4j database.

Prerequisites
- Python 3.12 or newer
- Git (optional)
- Docker & docker-compose (for running Neo4j locally)

Install

1. Create and activate a virtual environment (recommended):

   uv -m venv .venv
   source .venv/bin/activate

2. Install the project (uses pyproject.toml dependencies):

   uv -m pip install --upgrade pip
   uv -m pip install .

Configuration

The app reads configuration from a .env file in the project root. Required settings:

- NEO4J_URI (optional, default: neo4j://localhost:7687)
- NEO4J_USERNAME (required)
- NEO4J_PASSWORD (required)
- MCP_HOST (optional, default: 127.0.0.1)
- MCP_PORT (optional, default: 8000)
- DEBUG_MODE (optional, true/false)
- OPENAI_API_KEY (optional — if used by agents or other code)

Example .env

NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_neo4j_password
NEO4J_URI=neo4j://localhost:7687
MCP_HOST=127.0.0.1
MCP_PORT=8000
DEBUG_MODE=false

Run Neo4j with docker-compose

A basic docker-compose.yaml is included for running a local Neo4j instance. Before starting, edit the compose file to set the mapped host paths and credentials as desired.

Start Neo4j:

  docker-compose up -d

The compose maps the Neo4j HTTP console to 7474 and the bolt port to 7687 by default.

Run the MCP server

Start the server with the main entrypoint:

  uv main.py

By default the server runs using FastMCP and the transport configured in main.py ("streamable-http"). The host and port are taken from the .env or defaults in app/config.py.

Run the demo client

A simple demo client is provided to exercise the code:

  uv demo_client.py

Project layout (important files)

- main.py                - server entrypoint
- demo_client.py         - minimal demo client to run agents
- docker-compose.yaml    - example Neo4j service definition
- app/config.py          - configuration (pydantic-settings)
- app/mcp.py             - MCP application instance
- client/                - demo client/agent code

Notes

- The project depends on Neo4j and expects valid Neo4j credentials configured via environment variables or a .env file.
- If you change dependencies, update pyproject.toml and reinstall.

If you need a more detailed developer guide or example requests for the MCP endpoints, mention which areas to expand.
