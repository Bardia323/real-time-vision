import json
from pathlib import Path
from sys import platform
from typing import Optional
import psutil
import torch
from pydantic import BaseConfig, BaseModel, validator


class DeforumConfig(BaseModel):
    model_path: Optional[str] = "stabilityai/stable-diffusion-xl-base-0.9"
    num_gpus: Optional[int] = 1
    num_workers_per_gpu: Optional[int] = 1
    torch_dtype: Optional[torch.dtype] = torch.float16
    torch_device: torch.device = torch.device(
        "mps" if platform == "darwin" else ("cuda" if torch.cuda.is_available() else "cpu")
    )
    enable_attention_slicing: Optional[bool] = False
    enable_xformers_memory_efficient_attention: Optional[bool] = False
    compile_unet: Optional[bool] = False

    class Config(BaseConfig):
        arbitrary_types_allowed = True

    def to_json(self, path: Optional[str] = None, **dump_kwargs):
        json_ = json.dumps(
            {
                "torch_device": self.torch_device.type,
                "torch_dtype": str(self.torch_dtype).split(".")[-1],
                **self.dict(exclude={"torch_device", "torch_dtype"}),
            },
            **dump_kwargs
        )
        if path is None:
            return json_
        Path(path).write_text(json_)
        return json_

    @validator("torch_dtype", pre=True)
    def validate_torch_dtype(cls, v):
        if isinstance(v, str):
            return getattr(torch, v)
        return v

    @validator("torch_device", pre=True)
    def validate_torch_device(cls, v):
        if isinstance(v, str):
            return torch.device(v)
        return v


def create_config():
    config = DeforumConfig()

    # Enable attention slicing for systems with less than 64 GB of RAM
    total_memory_in_GB = psutil.virtual_memory().total / 1e9
    config.enable_attention_slicing = total_memory_in_GB < 64

    # Set the number of GPUs
    config.num_gpus = torch.cuda.device_count()

    # Write the configuration to a JSON file
    config.to_json("config.json", indent=4)


if __name__ == "__main__":
    create_config()
    DeforumConfig.parse_file("config.json")
