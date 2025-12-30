@echo off
REM Navigate to the agent directory
cd /d %~dp0\..\..

REM Run the agent using uv
uv run python demo_agent_os.py
