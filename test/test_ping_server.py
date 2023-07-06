import requests
import time
import json
import base64

n = 1  # number of seconds to wait between requests

while True:
    # load settings
    with open('settings.json', 'r') as f:
        settings = json.load(f)

    # post request to server
    try:
        response = requests.post("http://localhost:8000/api/generate", json=settings)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed due to an error: {e}")
        break

    # save returned image
    try:
        img_data = base64.b64decode(response.json()["image"])
        with open("results.png", "wb") as f:
            f.write(img_data)
    except Exception as e:
        print(f"Failed to save image due to error: {e}")
        break

    time.sleep(n)