from fastapi.middleware.cors import CORSMiddleware

from ..modules.default import default_router
from ..modules.users import users_router
from ..modules.notebooks import notebooks_router
from ..modules.tickets import tickets_router
from ..modules.security import security_router


def tune_routers(app):
    # app.include_router(default_router, tags=['default'])
    app.include_router(users_router, tags=['users'], prefix='/users')
    app.include_router(notebooks_router, tags=['notebooks'], prefix='/notebooks')
    app.include_router(tickets_router, tags=['tickets'], prefix='/tickets')
    app.include_router(security_router, tags=['security'])


def tune_cors(app):
    origins = [
        "http://localhost:8080"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
