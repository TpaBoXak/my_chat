from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
import json


from config import settings

from app import db_helper
from app.dao import chats as chat_dao
from app.utils.check_users import get_current_user

router: APIRouter = APIRouter(prefix=settings.api.chat_prefix)

@router.get("/by_user")
async def get_chats_by_user(
    session: AsyncSession = Depends(db_helper.session_getter),
    user_id: int = Depends(get_current_user)
):
    data = await chat_dao.get_chats_by_user(session=session, user_id=user_id)
    return JSONResponse(content=jsonable_encoder(data),
            status_code=status.HTTP_201_CREATED)