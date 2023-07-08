import requests
import time
import json
import base64

n = 0.0  # number of seconds to wait between requests

volta_request = {
  "data": {
    "prompt": "cat sushi dog",
    "scheduler": 1,
    "id": "string",
    "negative_prompt": "",
    "width": 1024,
    "height": 512,
    "steps": 10,
    "guidance_scale": 7,
    "self_attention_scale": 0,
    "seed": 10,
    "batch_size": 1,
    "batch_count": 1
  },
  "model": "dreamlike-art--dreamlike-photoreal-2.0__1024x512x1",
  "websocket_id": None,
  "save_image": True,
  "flags": {}
}

while True:
    # start
    start_time = time.time()

    # load settings
    with open('settings.json', 'r') as f:
        settings = json.load(f)

    volta_request["data"]["prompt"] = settings["prompt"]

    # post request to server
    try:
        response = requests.post("http://localhost:5003/api/generate/txt2img", json=volta_request)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed due to an error: {e}")
        time.sleep(5)

    # end
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:0.2f} seconds")

    time.sleep(n)