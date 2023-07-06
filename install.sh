#!/bin/bash

# create a virtual environment
python -m venv venv

# activate the virtual environment
source venv/bin/activate

# install necessary packages
python -m pip install -r requirements.txt

# setup config
python server/config.py

# create desktop shortcuts
REPO_PATH=$(pwd)

# image-server
cat > ~/Desktop/image-server.desktop << EOL
[Desktop Entry]
Version=1.0
Name=image-server
Comment=Launch Image Server
Exec=gnome-terminal --working-directory=$REPO_PATH -e "bash -c 'source venv/bin/activate; python -m uvicorn server.app:app --reload --port 8000; exec bash'"
Icon=$REPO_PATH/icons/red_cube.png
Terminal=true
Type=Application
Categories=Application;
EOL

# Update the file permissions so it's executable
chmod +x ~/Desktop/image-server.desktop

# webui
cat > ~/Desktop/webui.desktop << EOL
[Desktop Entry]
Version=1.0
Name=webui
Comment=Launch Webui
Exec=gnome-terminal --working-directory=$REPO_PATH -e "bash -c 'source venv/bin/activate; streamlit run streamlit/app.py; exec bash'"
Icon=$REPO_PATH/icons/yellow_cone.png
Terminal=true
Type=Application
Categories=Application;
EOL

# Update the file permissions so it's executable
chmod +x ~/Desktop/webui.desktop