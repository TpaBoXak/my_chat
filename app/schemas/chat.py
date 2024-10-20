from pydantic import BaseModel
from typing import List, Optional

class ChatBaseSchema(BaseModel):
    name: str
    members: List[int]
    is_group: bool