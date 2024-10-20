from fastapi import APIRouter

from config import settings


router = APIRouter(prefix=settings.api.prefix)

# from .enter import router as v1_enter_router
# router.include_router(v1_enter_router)
