@echo off

REM change to script's directory
cd /d %~dp0

REM create a virtual environment
python -m venv venv

REM activate the virtual environment
call venv\Scripts\activate

REM install pytorch (please replace this command for the proper torch version for your system)
pip install --pre torch torchvision torchaudio -f https://download.pytorch.org/whl/nightly/cu121/torch_nightly.html

REM install necessary packages
python -m pip install -r requirements.txt

REM setup config
python diffusers-server\config.py

REM call vbs script to create shortcuts (probably useless)
REM cscript //nologo create_shortcuts.vbs

