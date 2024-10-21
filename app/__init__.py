from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
import redis.asyncio as redis
import socketio

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
main_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

redis_client = redis.Redis.from_url(settings.redis.url)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

from app.api import api_router
main_app.include_router(api_router)

from app.api import template_router
main_app.include_router(template_router)

from app.sockets.socket import sio
app = socketio.ASGIApp(sio, main_app)

