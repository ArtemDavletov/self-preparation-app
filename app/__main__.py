import uvicorn as uvicorn
from fastapi import FastAPI

from app.settings.database import Base, engine
from app.settings.settings import settings
from app.settings import tune


Base.metadata.create_all(bind=engine)

app = FastAPI()

tune.tune_cors(app=app)
tune.tune_routers(app=app)


if __name__ == '__main__':
    uvicorn.run(
        '__main__:app',
        host=settings.APP_HOST,
        reload=settings.DEBUG_MODE,
        port=settings.APP_PORT,
    )
