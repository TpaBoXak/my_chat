from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from typing import List


from config import settings

from app import db_helper
from app.dao import chats as chat_dao
from app.dao import message as message_dao
from app.utils.check_users import get_current_user
from app.schemas.chat import ChatBaseSchema
from app.schemas.messages import MessageSchema

router: APIRouter = APIRouter(prefix=settings.api.chat_prefix)

@router.get("/by_user")
async def get_chats_by_user(
    session: AsyncSession = Depends(db_helper.session_getter),
    user_id: int = Depends(get_current_user)
):
    data = await chat_dao.get_chats_by_user(session=session, user_id=user_id)
    return JSONResponse(content=jsonable_encoder(data),
            status_code=status.HTTP_201_CREATED)


@router.post("/add")
async def add_chat(
    chat_schema: ChatBaseSchema,
    session: AsyncSession = Depends(db_helper.session_getter),
    user_id: int = Depends(get_current_user),
):
    chat_id: Optional[int]  = await chat_dao.add_chat(
        session=session, chat_schema=chat_schema)
    
    if not chat_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect input chat data",
        )
    
    if not await chat_dao.add_users_to_chat(session=session,
            chat_schema=chat_schema, chat_id=chat_id, user_id=user_id):
        chat_dao.delete_chat(session=session, chat_id=chat_id)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect input membres data",
        )
    
    return {"message": "chat successfully completed"}
    
@router.get("/{chat_id}/messages", response_model=List[MessageSchema])
async def get_chat_messages(
    chat_id: int, 
    session: AsyncSession = Depends(db_helper.session_getter),
    user_id: int = Depends(get_current_user)
):
    messages: List[MessageSchema] = await message_dao. \
            messages_by_chat_id(session=session, chat_id=chat_id)
    return messages