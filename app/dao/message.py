from sqlalchemy.ext.asyncio import AsyncSession
from app.models.message import Message
from app.models.user import User
from app.schemas.messages import MessageSchema

from sqlalchemy import select


async def delete_message_by_chat(session: AsyncSession, chat_id: int) -> bool:
    try:
        stmt = select(Message).where(Message.chat_id == chat_id)
        messsages: list[Message] = session.execute(stmt)

        for messsage in messsages:
            session.delete(messsage)
    except:
        session.rollback()
        return False
    else:
        session.commit()
        return True
    

async def messages_by_chat_id(
    session: AsyncSession, chat_id: int
) -> list[MessageSchema]:
    stmt = select(User.id, User.first_name, User.second_name, Message.chat_id,
            Message.content).where(Message.chat_id == chat_id).\
            select_from(Message).join(User, Message.user_id == User.id).\
            order_by(Message.time_created.asc())
    messages_user: list[tuple] = await session.execute(stmt)

    messages: list[MessageSchema] = []
    for msg_u in messages_user:
        message: MessageSchema = MessageSchema(
            user_id=msg_u[0], first_name=msg_u[1], second_name=msg_u[2],
            chat_id=msg_u[3], text=msg_u[4]
        )
        messages.append(message)

    return messages


