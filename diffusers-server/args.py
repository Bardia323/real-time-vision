from typing import Optional
from pydantic import BaseModel
from enum import Enum
from diffusers.schedulers import (
    EulerAncestralDiscreteScheduler,
    EulerDiscreteScheduler,
    DPMSolverMultistepScheduler,
    DPMSolverSinglestepScheduler,
    DDIMScheduler,
    PNDMScheduler,
    LMSDiscreteScheduler,
    UniPCMultistepScheduler
)

class SchedulerType(Enum):
    EULER_ANCESTRAL = "euler_ancestral"
    EULER = "euler"
    PNDM = "pndm"
    DPMPP_SINGLESTEP = "dpmpp_singlestep"
    DPMPP_MULTISTEP = "dpmpp_multistep"
    LMS = "lms"
    DDIM = "ddim"
    UNIPC = "unipc"

    @classmethod
    def to_scheduler(self, value):
        opts = {
            self.EULER_ANCESTRAL.value: EulerAncestralDiscreteScheduler,
            self.EULER.value: EulerDiscreteScheduler,
            self.DDIM.value: DDIMScheduler,
            self.PNDM.value: PNDMScheduler,
            self.DPMPP_MULTISTEP.value: DPMSolverMultistepScheduler,
            self.DPMPP_SINGLESTEP.value: DPMSolverSinglestepScheduler,
            self.LMS.value: LMSDiscreteScheduler,
            self.UNIPC.value: UniPCMultistepScheduler
        }
        return opts.get(value, EulerAncestralDiscreteScheduler)

class DeforumArgs(BaseModel):
    prompt: str
    negative_prompt: Optional[str] = ""
    num_inference_steps: Optional[int] = 50
    guidance_scale: Optional[float] = 7.5
    scheduler: SchedulerType = SchedulerType.EULER_ANCESTRAL
    return_image_as_bytes: Optional[bool] = False
    width: Optional[int] = 512
    height: Optional[int] = 512