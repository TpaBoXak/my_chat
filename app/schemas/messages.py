from pydantic import BaseModel

class MessageSchema(BaseModel):
    chat_id: int
    user_id: int
    first_name: str
    second_name: str
    text: str

class AddMesageSchema(BaseModel):
    chat_id: int
    text: str
    token: str