from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import status

from config import settings

from app import db_helper
from app.schemas.users import UserBaseSchema
from app.dao import users as user_dao
from app.jwt import jwt as jwt_confirm
from app.models import User

router: APIRouter = APIRouter(prefix=settings.api.enter_prefix)

@router.post("")
async def add_user(user_schema: UserBaseSchema, 
    session: AsyncSession = Depends(db_helper.session_getter)
):
    user: User = await user_dao.get_user_by_nickname(session=session, 
            nickname=user_schema.nickname)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect nickname or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if not await jwt_confirm.verify_password(user_schema.password,
            user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect nickname or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not await user_dao.add_user(session=session, ):
        data = {"message": "Error creating user"}
        return HTTPException(status_code=500, detail=data)
    
    data = {"message" "Success creating user"}
    return data