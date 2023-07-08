#!/bin/bash

# create a virtual environment
python -m venv venv

# activate the virtual environment
source venv/bin/activate

# install pytorch
pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu121

# install necessary packages
python -m pip install -r requirements.txt

# setup config
python image-server/config.py

# create desktop shortcuts
REPO_PATH=$(pwd)

# image-server
cat > ~/Desktop/image-server.desktop << EOL
[Desktop Entry]
Version=1.0
Name=image-server
Comment=Launch Image Server
Exec=gnome-terminal --working-directory=$REPO_PATH -- bash $REPO_PATH/launch-image-server.sh
Icon=$REPO_PATH/icons/red_cube.png
Terminal=true
Type=Application
Categories=Application;
EOL

# Update the file permissions so it's executable
chmod +x launch-image-server.sh
chmod +x ~/Desktop/image-server.desktop

# image-polling
cat > ~/Desktop/image-polling.desktop << EOL
[Desktop Entry]
Version=1.0
Name=image-polling
Comment=Launch Image Polling
Exec=gnome-terminal --working-directory=$REPO_PATH -- bash $REPO_PATH/launch-image-polling.sh
Icon=$REPO_PATH/icons/red_cube.png
Terminal=true
Type=Application
Categories=Application;
EOL

# Update the file permissions so it's executable
chmod +x launch-image-polling.sh
chmod +x ~/Desktop/image-polling.desktop

# whisper-server
cat > ~/Desktop/whisper-server.desktop << EOL
[Desktop Entry]
Version=1.0
Name=whisper-server
Comment=Launch Whisper Server
Exec=gnome-terminal --working-directory=$REPO_PATH -- bash $REPO_PATH/launch-whisper-server.sh
Icon=$REPO_PATH/icons/blue_sphere.png
Terminal=true
Type=Application
Categories=Application;
EOL

# Update the file permissions so it's executable
chmod +x launch-whisper-server.sh
chmod +x ~/Desktop/whisper-server.desktop

# whisper-client
cat > ~/Desktop/whisper-client.desktop << EOL
[Desktop Entry]
Version=1.0
Name=whisper-client
Comment=Launch Whisper Client
Exec=gnome-terminal --working-directory=$REPO_PATH -- bash $REPO_PATH/launch-whisper-client.sh
Icon=$REPO_PATH/icons/blue_sphere.png
Terminal=true
Type=Application
Categories=Application;
EOL

# Update the file permissions so it's executable
chmod +x launch-whisper-server.sh
chmod +x ~/Desktop/whisper-client.desktop

# webui
cat > ~/Desktop/webui.desktop << EOL
[Desktop Entry]
Version=1.0
Name=webui
Comment=Launch Webui
Exec=gnome-terminal --working-directory=$REPO_PATH -- bash $REPO_PATH/launch-webui.sh
Icon=$REPO_PATH/icons/yellow_cone.png
Terminal=true
Type=Application
Categories=Application;
EOL

# Update the file permissions so it's executable
chmod +x launch-webui.sh
chmod +x ~/Desktop/webui.desktop

# dreambooth
cat > ~/Desktop/real-time-vision.desktop << EOL
[Desktop Entry]
Version=1.0
Name=real-time-vision
Comment=Launch Real Time Vision
Exec=gnome-terminal --working-directory=$REPO_PATH -- bash $REPO_PATH/launch-real-time-vision.sh
Icon=$REPO_PATH/icons/deforum.jpg
Terminal=true
Type=Application
Categories=Application;
EOL

# Update the file permissions so it's executable
chmod +x launch-real-time-vision.sh
chmod +x ~/Desktop/real-time-vision.desktop