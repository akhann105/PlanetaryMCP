Start-Process powershell -ArgumentList "-NoExit", "-Command", ".\.venv\Scripts\python.exe mongo_app.py"

Start-Process powershell -ArgumentList "-NoExit", "-Command", ".\.venv\Scripts\python.exe redis_app.py"

Start-Process powershell -ArgumentList "-NoExit", "-Command", ".\.venv\Scripts\python.exe mcp_server.py"