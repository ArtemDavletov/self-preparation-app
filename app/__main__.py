import uvicorn as uvicorn
from fastapi import FastAPI

from app.settings.database import Base, engine
from app.settings.settings import settings

from app.modules.dafault import default_router
from app.modules.users import users_router
from app.modules.notebooks import notebooks_router
from app.modules.tickets import tickets_router


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(default_router, tags=['default'])
app.include_router(users_router, tags=['users'], prefix='/users')
app.include_router(notebooks_router, tags=['notebooks'], prefix='/notebooks')
app.include_router(tickets_router, tags=['tickets'], prefix='/tickets')


if __name__ == '__main__':
    uvicorn.run(
        '__main__:app',
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )
