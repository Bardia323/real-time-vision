#!/bin/bash

# activate the virtual environment
source venv/bin/activate

# Define the repo path. Change this to your actual repo path.
REPO_PATH=$(pwd)

# Launch the first process (diffusers server)
gnome-terminal --working-directory=$REPO_PATH -- bash $REPO_PATH/launch-diffusers-server.sh &

sleep 5

# Launch the second process (diffusers polling)
gnome-terminal --working-directory=$REPO_PATH -- bash $REPO_PATH/launch-diffusers-polling.sh &

sleep 5

# Launch the third process (whisper server)
gnome-terminal --working-directory=$REPO_PATH -- bash $REPO_PATH/launch-whisper-server.sh &

sleep 5

# Launch the fourth process (whisper client)
gnome-terminal --working-directory=$REPO_PATH -- bash $REPO_PATH/launch-whisper-client.sh &

sleep 5

# Launch the fifth process (display)
gnome-terminal --working-directory=$REPO_PATH -- bash $REPO_PATH/launch-display.sh &

sleep 5

# Wait for all processes to finish
wait