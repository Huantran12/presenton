from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from enums.image_provider import ImageProvider


class ImageProviderTestConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    IMAGE_PROVIDER: ImageProvider
    OPENAI_API_KEY: str = Field(default="", repr=False)
    GOOGLE_API_KEY: str = Field(default="", repr=False)
    PEXELS_API_KEY: str = Field(default="", repr=False)
    PIXABAY_API_KEY: str = Field(default="", repr=False)
    COMFYUI_URL: str = ""
    COMFYUI_WORKFLOW: str = ""
    OPEN_WEBUI_IMAGE_URL: str = ""
    OPEN_WEBUI_IMAGE_API_KEY: str = Field(default="", repr=False)
    OPENAI_COMPAT_IMAGE_BASE_URL: str = ""
    OPENAI_COMPAT_IMAGE_API_KEY: str = Field(default="", repr=False)
    OPENAI_COMPAT_IMAGE_MODEL: str = ""
    GPT_IMAGE_2_QUALITY: Literal["low", "medium", "high"] = "medium"
    GPT_IMAGE_1_5_QUALITY: Literal["low", "medium", "high"] = "medium"
