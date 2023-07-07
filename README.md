# Real-Time-Vision

## Step 1: Git Clone

Clone the repository on your local machine using:

```
git clone https://github.com/deforum/real-time-vision.git
```
Then, go to the cloned directory:

```
cd real-time-vision
```

## Step 2: Run install.sh

Execute the install.sh script:

```
bash install.sh
```

## Step 3: Install portaudio

Use the following command:
```
apt-get install portaudio19-dev -y
```

## Step 4: Log in to Huggingface

Use the following command:

```
huggingface-cli login --token <insert_access_token>
```

Make sure to replace `<insert_access_token>` with your actual Huggingface token.

## Real-Time Audio to Image

For real-time audio to image you will need to launch the following applications in order:

```
bash launch-image-server.sh
```
```
bash launch-image-polling.sh
```
```
bash launch-whisper-server.sh
```
```
bash launch-whisper-client.sh
```
## Webui 

For webui you will need to launch the image server and the webui. Optionally you can launch the image polling.
```
bash launch-image-server.sh
```
```
bash launch-webui.sh
```