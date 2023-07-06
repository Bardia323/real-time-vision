import torch
from diffusers import DiffusionPipeline
from diffusers import EulerAncestralDiscreteScheduler

import cProfile
import pstats
import io
from pstats import SortKey

path = 'dreamlike-art/dreamlike-photoreal-2.0'
prompt = "Women standing on a mountain top"

torch.set_grad_enabled(False)
torch.backends.cudnn.benchmark = True

with torch.inference_mode():
    pipe = DiffusionPipeline.from_pretrained(path, torch_dtype=torch.float16, safety_checker=None, requires_safety_checker=False)
    pipe.to('cuda')
    pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
    pipe.unet.to(device='cuda', dtype=torch.float16, memory_format=torch.channels_last)

    for bi in range(7):
        if bi == 2:      # Start profiler on 3rd image
            ob = cProfile.Profile()
            ob.enable()
        images = pipe(prompt=prompt, width=512, height=512, num_inference_steps=5, num_images_per_prompt=1)
    ob.disable()
    sec = io.StringIO()
    sortby = SortKey.TIME
    ps = pstats.Stats(ob, stream=sec).sort_stats(sortby)
    ps.print_stats()
    print(sec.getvalue()[0:1000]) 