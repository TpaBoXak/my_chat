from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User

from sqlalchemy import select


async def get_user_by_nickname(session: AsyncSession, nickname: str):
    stmt = select(User).where(User.nickname == nickname)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()
    return user
