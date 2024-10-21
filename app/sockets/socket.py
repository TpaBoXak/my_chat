import socketio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import Depends
from fastapi import HTTPException
from jose import JWTError

from app import db_helper
from app.schemas.messages import MessageSchema
from app.schemas.messages import AddMesageSchema
from app.models.message import Message
from app.utils.check_users import get_current_user
from app.dao import users as user_dao
from app.models.user import User



sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins="*")
@sio.event
async def join(sid, chat_id: str):
    print(f"Клиент {sid} присоединился к чату {chat_id}")
    await sio.enter_room(sid, chat_id)

@sio.event
async def send_message(
    sid, data: dict
):
    try:
        user_id = await get_current_user(token=data["token"])
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    async with db_helper.session_getter_context() as session:
        user_id = await get_current_user(data["token"])
        message: Message = Message()
        message.chat_id = int(data["chat_id"])
        message.content = data["text"]
        message.user_id = user_id

        session.add(message)
        await session.commit()
        await session.refresh(message)

        user: User = await user_dao.get_user_by_id(session=session,
                user_id=user_id)
        
        returned_message: dict = {
            "chat_id": int(data["chat_id"]),
            "text": data["text"],
            "user_id": user_id,
            "first_name": user.first_name,
            "second_name": user.second_name
        }
        
        await sio.emit("receive_message", returned_message,
                room=data["chat_id"])
        print(f"Sending message to chat {data['chat_id']}")