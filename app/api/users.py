from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
import json

from app.utils.check_users import get_current_user

from config import settings

from app import db_helper
from app.dao import users as user_dao

router: APIRouter = APIRouter(prefix=settings.api.users_prefix)

@router.get("/all")
async def get_all_users(
    session: AsyncSession = Depends(db_helper.session_getter),
    user_id: int = Depends(get_current_user)
):
    data = await user_dao.get_all_user(session=session, user_id=user_id)
    return JSONResponse(content=jsonable_encoder(data),
            status_code=status.HTTP_201_CREATED)