import base64
import requests
import concurrent.futures
import time

# Define the arguments you want to send
args_list = [
    {"prompt": "a photo of an astronaut riding a horse on mars", "strength": 1.0, "height": 1024, "width": 1024, "num_inference_steps": 20},
    {"prompt": "a photo of a robot playing soccer", "strength": 0.9, "height": 1024, "width": 1024, "num_inference_steps": 20},
    {"prompt": "a photo of a cat surfing", "strength": 0.8, "height": 1024, "width": 1024, "num_inference_steps": 20},
    # add more arguments as needed
]

def make_request(args):
    """
    Makes a POST request to the specified API with given arguments.
    """
    try:
        response = requests.post("http://localhost:8000/api/generate", json=args)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed due to an error: {e}")
        return None
    return response

def save_image(response, i):
    """
    Saves the response content as an image.
    """
    try:
        img_data = base64.b64decode(response.json()["image"])
        with open(f"test_mulitple_queries_{i}.png", "wb") as f:
            f.write(img_data)
    except Exception as e:
        print(f"Failed to save image due to error: {e}")

def main():
    # Start timing
    start_time = time.time()

    # Use a ThreadPoolExecutor to send the requests concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(make_request, args) for args in args_list]

    # Wait for all requests to complete and get the responses
    responses = [f.result() for f in futures]

    # Save the response content as images
    for i, response in enumerate(responses):
        if response is not None:
            save_image(response, i)
        else:
            print(f"Skipping image {i} due to failed request")

    # End timing and print execution time
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
