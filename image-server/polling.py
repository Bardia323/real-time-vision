import requests
import time
import json
import base64
import time

n = 0.1  # number of seconds to wait between requests

while True:

    # start
    start_time = time.time()

    # load settings
    with open('settings.json', 'r') as f:
        settings = json.load(f)

    # post request to server
    try:
        response = requests.post("http://localhost:8000/api/generate", json=settings)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed due to an error: {e}")
        time.sleep(5)

    # save returned image
    try:
        img_data = base64.b64decode(response.json()["image"])
        with open("results.png", "wb") as f:
            f.write(img_data)
    except Exception as e:
        print(f"Failed to save image due to error: {e}")
        time.sleep(5)

    # end
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:0.2f} seconds")

    time.sleep(n)