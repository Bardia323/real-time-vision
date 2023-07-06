import io
import json
import base64
import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import ValidationError
from diffusers import DiffusionPipeline
import ray
import torch
from .config import DeforumConfig
from .args import DeforumArgs

global current_worker
global lock

torch.set_grad_enabled(False)
torch.backends.cudnn.benchmark = True
torch.backends.cuda.matmul.allow_tf32 = True
torch.set_float32_matmul_precision("medium")

# Load the configuration
with open('./config.json') as f:
    config_data = json.load(f)

try:
    config = DeforumConfig(**config_data)
except ValidationError as e:
    raise HTTPException(status_code=500, detail=f"Error loading configuration: {e}")

# Initialize Ray
ray.init(num_gpus=config.num_gpus)

# Define the remote class
@ray.remote(num_gpus=1/config.num_workers_per_gpu)
class ImageGenerator:
    def __init__(self, config: DeforumConfig):
        self.pipeline = DiffusionPipeline.from_pretrained(
                config.model_path, 
                torch_dtype=config.torch_dtype
        )

        # Optional Optimizations
        if config.compile_unet:
            self.pipeline.unet = torch.compile(self.pipeline.unet, mode="reduce-overhead", fullgraph=True)
        if config.enable_xformers_memory_efficient_attention:
            self.pipeline.enable_xformers_memory_efficient_attention()
        if config.enable_attention_slicing:
            self.pipeline.enable_attention_slicing()

        # Optimizations
        self.pipeline.unet.to(memory_format=torch.channels_last)
        self.pipeline.vae.to(memory_format=torch.contiguous_format)

        # Move the pipeline to the GPU (or cpu) 
        self.pipeline = self.pipeline.to(config.torch_device)
        
    def generate(self, args: DeforumArgs):
        args_dict = args.dict()
        args_dict.pop("return_image_as_bytes",None)
        scheduler = args_dict.pop("scheduler",None)
        if scheduler is not None:
            self.pipeline.scheduler = args.scheduler.to_scheduler(args.scheduler).from_config(self.pipeline.scheduler.config)
        with torch.inference_mode():
            image = self.pipeline(**args_dict).images[0]
        return image

# Initialize the workers
workers = [ImageGenerator.remote(config) for _ in range(config.num_gpus*config.num_workers_per_gpu)]
current_worker = 0

app = FastAPI()
lock = asyncio.Lock()

@app.post("/api/generate")
async def generate(args: DeforumArgs):
    async with lock:
        global current_worker
        current_worker += 1
    # Assign the request to the current worker
    image = await workers[current_worker % (config.num_gpus*config.num_workers_per_gpu)].generate.remote(args)
    # Update the current worker
    iob = io.BytesIO()
    image.save(iob, format='PNG')
    iob.seek(0)
    if args.return_image_as_bytes:
        return StreamingResponse(iob, media_type="image/png")
    img_str = base64.b64encode(iob.getvalue()).decode()
    return {"image": img_str}
