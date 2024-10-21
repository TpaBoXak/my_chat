from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy import func
from typing import Optional

from app.models.chat import Chat
from app.dao import message as message_dao
from app.models.chat import UserChat
from app.schemas.chat import ChatBaseSchema

async def get_chats_by_user(session: AsyncSession, user_id: int):
    stmt = select(Chat.id, Chat.title).\
            where(Chat.is_group).join(UserChat,
            UserChat.user_id == user_id).select_from(Chat)
    users_info: list[tuple] = await session.execute(stmt)
    
    result = {}
    for row in users_info:
        result[row[0]] = {
            "title": row[1],
        }

    return result


async def add_chat(
    session: AsyncSession, chat_schema: ChatBaseSchema
) -> Optional[int]:
    try:
        chat: Chat = Chat()
        chat.is_group = chat_schema.is_group
        chat.title = chat_schema.title
        session.add(chat)
    except:
        await session.rollback()
        return None
    else:
        await session.commit()
        return chat.id
        

async def add_users_to_chat(
    session: AsyncSession, chat_schema: ChatBaseSchema, chat_id: int,
    user_id: int
) -> bool:
    try:
        for member in chat_schema.members:
            user_chat: UserChat = UserChat()
            user_chat.chat_id = chat_id
            user_chat.user_id = member
            session.add(user_chat)
        
        user_chat: UserChat = UserChat()
        user_chat.chat_id = chat_id
        user_chat.user_id = user_id
        session.add(user_chat)
    except:
        await session.rollback()
        return False
    else:
        await session.commit()
        return True
    

async def delete_chat(
    session: AsyncSession, chat_id: int
) -> None:
    try:
        stmt = select(UserChat).where(UserChat.chat_id == chat_id)
        users_chats: list[UserChat] = session.execute(stmt)
        message_dao.delete_message_by_chat(session=session, chat_id=chat_id)

        for user_chat in users_chats:
            session.delete(user_chat)
    except:
        session.rollback()
    else:
        session.commit()