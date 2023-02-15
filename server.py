import uvicorn
from fastapi import FastAPI

from routers import students, subjects
from starlette.middleware.cors import CORSMiddleware


# Module variables
app = FastAPI()

origins = ["http://localhost:8000",
"http://localhost:3000",
"http://localhost:3001",
"http://localhost:3002"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    students.router,
    prefix="/Students",
    tags=["Students"],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    subjects.router,
    prefix="/Subjects",
    tags=["Subjects"],
    responses={404: {"description": "Not found"}},
)


def start(ip: str = 'localhost', port: int = 8000) -> None:
    """Starts a Uvicorn ASGI RESTful server.

    Args:
        ip (str): IP address or hostname.
        port (int): Listening port.
    """
    uvicorn.run(
        'server:app',
        host=ip,
        port=port,
        log_level='info'
    )
