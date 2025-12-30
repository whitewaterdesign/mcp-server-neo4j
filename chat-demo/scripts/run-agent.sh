#!/bin/bash

# Navigate to the agent directory
cd "$(dirname "$0")/../.." || exit 1

# Run the agent using uv
uv run python demo_agent_os.py
