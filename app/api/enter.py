# from fastapi import APIRouter
# from fastapi import Depends
# from fastapi import HTTPException
# from sqlalchemy.ext.asyncio import AsyncSession

# from config import settings

# from app import db_helper
# from app.schemas.users import UserCreate
# from app.dao import users as user_dao

# router: APIRouter = APIRouter(prefix=settings.api.enter_prefix)

# @router.post("")
# async def add_user(create_user: UserCreate, 
#     session: AsyncSession = Depends(db_helper.session_getter)
# ):
#     if not await user_dao.add_user(session=session, tg_id=create_user.tg_id):
#         data = {"message": "Error creating user"}
#         return HTTPException(status_code=500, detail=data)
    
#     data = {"message" "Success creating user"}
#     return data