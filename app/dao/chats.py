from sqlalchemy.ext.asyncio import AsyncSession
from app.models.chat import Chat
from app.models.chat import UserChat

from sqlalchemy import select

async def get_chats_by_user(session: AsyncSession, user_id: int):
    stmt = select(Chat).where(Chat.is_group).join(UserChat, UserChat.user_id == user_id)
    users_info: list[tuple] = await session.execute(stmt)
    
    result = {}
    for row in users_info:
        result[row[0]] = {
            "first_name": row[1],
            "second_name": row[2],
            "nickname": row[3]
        }

    return result

