@echo off

REM change to script's directory
cd /d %~dp0

REM activate the virtual environment
call ..\venv\Scripts\activate

REM add the parent directory to PYTHONPATH
set PYTHONPATH=..;%PYTHONPATH%

REM launch image-server
python -m uvicorn diffusers-server.app:app --reload --port 8000