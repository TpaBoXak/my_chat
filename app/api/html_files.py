from fastapi import Request
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from config import settings

router: APIRouter = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/login", response_class=HTMLResponse)
async def get_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/home", response_class=HTMLResponse)
async def get_home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@router.get("/create-chat", response_class=HTMLResponse)
async def get_create_chat_page(request: Request):
    return templates.TemplateResponse("create_chat.html", {"request": request})

@router.get("/chat/{chat_id}", response_class=HTMLResponse)
async def get_chat_page(request: Request, chat_id: int):
    return templates.TemplateResponse("chat.html", {"request": request})
