#!/bin/bash

# activate the virtual environment
source venv/bin/activate

# launch image-server
python -m uvicorn image-server.app:app --reload --port 8000