#!/bin/bash

# Store path of the current script as REPO_PATH
REPO_PATH=$(pwd)

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