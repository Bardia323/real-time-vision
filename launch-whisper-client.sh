#!/bin/bash

# activate the virtual environment
source venv/bin/activate

# launch whisper-server
python whisper/client.py --host localhost --port 9090