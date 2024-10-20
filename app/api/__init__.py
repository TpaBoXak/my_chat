from fastapi import APIRouter

from config import settings


router = APIRouter(prefix=settings.api.prefix)

from .auth import router as auth_router
router.include_router(auth_router)
