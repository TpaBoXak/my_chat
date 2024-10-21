from pydantic import BaseModel
from typing import List, Optional

class ChatBaseSchema(BaseModel):
    title: str
    members: List[int]
    is_group: bool