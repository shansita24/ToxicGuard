from pydantic import BaseModel
from typing import List


class TextRequest(BaseModel):
    text: str


class BatchRequest(BaseModel):
    texts: List[str]