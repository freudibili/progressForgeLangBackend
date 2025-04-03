from pydantic import BaseModel
from typing import Dict

class Level(BaseModel):
    id: str
    name: str

    class Config:
        from_attributes = True

class Vocabulary(BaseModel):
    id: str
    infinitiv: Dict[str, str]
    level_id: str
    type: str
    example: Dict[str, str]

    class Config:
        from_attributes = True 