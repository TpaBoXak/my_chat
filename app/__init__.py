from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordBearer
import redis.asyncio as redis

from app.models import DataBaseHelper
from config import settings
from .models import Base


db_helper = DataBaseHelper(
        url=str(settings.db.url),
        echo=settings.db.echo,
        echo_pool=settings.db.echo_pool,
        pool_size=settings.db.pool_size,
        max_overflow=settings.db.max_overflow,
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    print(str(settings.db.url))
    yield
    # shutdown
    print("dispose engine")
    await db_helper.dispose()

main_app = FastAPI(lifespan=lifespan)
redis_client = redis.Redis.from_url(settings.redis.url)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

from app.api import api_router
main_app.include_router(api_router)

from app.api import template_router
main_app.include_router(template_router)

