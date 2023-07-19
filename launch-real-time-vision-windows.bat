@echo off

REM change to script's directory
cd /d %~dp0

REM activate the virtual environment
call venv\Scripts\activate

REM Define the repo path. Change this to your actual repo path.
set REPO_PATH=%cd%

REM Define the scripts path
set SCRIPTS_PATH=%REPO_PATH%\win-scripts

REM Launch the first process (diffusers server)
start cmd /k "cd /d %SCRIPTS_PATH% & call launch-diffusers-server.cmd"
timeout /t 5 /nobreak

REM Launch the second process (diffusers polling)
start cmd /k "cd /d %SCRIPTS_PATH% & call launch-diffusers-polling.cmd"
timeout /t 5 /nobreak

REM Launch the third process (whisper server)
start cmd /k "cd /d %SCRIPTS_PATH% & call launch-whisper-server.cmd"
timeout /t 5 /nobreak

REM Launch the fourth process (whisper client)
start cmd /k "cd /d %SCRIPTS_PATH% & call launch-whisper-client.cmd"
timeout /t 5 /nobreak

REM Launch the fifth process (display)
start cmd /k "cd /d %SCRIPTS_PATH% & call launch-display.cmd"
timeout /t 5 /nobreak
