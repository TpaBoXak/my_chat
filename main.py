import uvicorn
from app import main_app
from config import settings


if __name__ == "__main__":
    uvicorn.run(app="main:main_app", reload=True,
            host=settings.run.host,
            port=settings.run.port)