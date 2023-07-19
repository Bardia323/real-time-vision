# Real-Time-Vision

This is a repository for Real-Time-Vision.
Real-Time-Vision is a practical and intriguing system that uses machine learning to turn spoken language into corresponding images in real time. Ideal for data visualization and communication enhancement, this tool offers a novel way to represent verbal information visually.

## Table of Contents
1. [Installation for Linux](#installation-for-linux)
2. [Installation for Windows](#installation-for-windows)

## Installation for Linux

### Step 1: Git Clone
Clone the repository on your local machine using:

```
git clone https://github.com/deforum/real-time-vision.git
```

Then, go to the cloned directory:

```
cd real-time-vision
```

### Step 2: Run install.sh
Execute the install.sh script:

```
bash install.sh
```

### Step 3: Install portaudio
Use the following command:

```
apt-get install portaudio19-dev -y
```

### Step 4: Log in to Huggingface
Use the following command:

```
huggingface-cli login --token <insert_access_token>
```

Make sure to replace `<insert_access_token>` with your actual Huggingface token.

### Real-Time Audio to Image
For real-time audio to image you will need to launch the following applications in order:
```
bash launch-image-server.sh

bash launch-image-polling.sh

bash launch-whisper-server.sh

bash launch-whisper-client.sh
```
Alternatively, you can run:
```
launch-real-time-vision.sh
```
### WebUI
For WebUI you will need to launch the image server and the WebUI. Optionally, you can launch the image polling.

```
bash launch-image-server.sh

bash launch-webui.sh
```

## Installation for Windows

### Step 1: Install PyTorch
Before proceeding, make sure to install the appropriate version of PyTorch for your system. You can find the installation instructions on the PyTorch official website: https://pytorch.org/get-started/locally/

### Step 2: Log in to Huggingface
Use the following command:

```
huggingface-cli login --token <insert_access_token>
```

Make sure to replace `<insert_access_token>` with your actual Huggingface token.

### Step 3: Run install-windows.cmd
Clone the repository onto your local machine using:

```
git clone https://github.com/deforum/real-time-vision.git
```

Then, navigate to the cloned directory:

```
cd real-time-vision
```

To install necessary packages and set up your environment, run the `install-windows.cmd` script:

```
install-windows.cmd
```

### Step 4: Initialize settings.json and config.json
Initialize your `settings.json` and `config.json` files in the `win-scripts` directory. These files should contain the appropriate configuration details required for the applications to run correctly.

### Step 5: Run launch-real-time-vision-windows.bat
Launch the Real-Time-Vision applications in the correct order by running the `launch-real-time-vision-windows.bat` script:

```
launch-real-time-vision-windows.bat
```

Now, the Real-Time-Vision system should be up and running on your Windows machine.
