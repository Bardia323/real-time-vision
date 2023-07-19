@echo off

REM change to script's directory
cd /d %~dp0

REM activate the virtual environment
call ..\venv\Scripts\activate

REM launch display
python ..\display\app.py
