import streamlit as st
import json
import requests
import base64
import time
import os

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

def save_image(response):
    """
    Saves the response content as an image.
    """
    try:
        img_data = base64.b64decode(response.json()["image"])
        directory = "outputs"
        # Create 'outputs' directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)
        # Get current time and format it to a string
        timestr = time.strftime("%Y%m%d-%H%M%S")
        with open(f"{directory}/result_{timestr}.png", "wb") as f:
            f.write(img_data)
    except Exception as e:
        print(f"Failed to save image due to error: {e}")


def save_settings(data, filename='settings.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    st.write(f'Settings saved to {filename}.')

def app():
    # title
    st.title('webui')

    # tabs
    tabs = st.tabs(["settings", "settings json"])

    # Initialize session state for text if not already done
    if 'text' not in st.session_state:
        st.session_state.text = ''

    settings = {
        'prompt': "",
        'negative_prompt': "",
        'guidance_scale': 5,
        'num_inference_steps': 20,
        'width': 1024,
        'height': 1024
    }

    with tabs[0]:
        # Get inputs from the user
        settings["prompt"] = st.text_area('Prompt')
        settings["negative_prompt"] = st.text_area('Negative Prompt')

        cols = st.columns(2)

        with cols[0]:
            settings["guidance_scale"] = st.number_input('Guidance Scale', value=5, step=1)
            settings["num_inference_steps"] = st.number_input('Steps', min_value=1, value=20, step=10)

        with cols[1]:
            settings["width"] = st.number_input('Width', min_value=64, value=1024, step=64)
            settings["height"] = st.number_input('Height', min_value=64, value=1024, step=64)

        # Save settings to json file when 'Save JSON' button is clicked
        if st.button('Run'):
            save_settings(settings)
            st.write('Running...')
            # Start timing
            start_time = time.time()
            response = make_request(settings)
            end_time = time.time()
            st.write(f"Execution time: {end_time - start_time:0.2f} seconds")
            save_image(response)
            img_data = base64.b64decode(response.json()["image"])
            st.image(img_data)  # Line added for displaying the image
            

    with tabs[1]:
        # show json
        st.json(settings)
            

if __name__ == '__main__':
    app()