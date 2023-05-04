
from os import environ

import uvicorn
from dotenv import dotenv_values
from fastapi import FastAPI

from src.config.database import engine
from src.model.index import metadata
from src.routes import routes

# table generator
metadata.create_all(bind=engine)

app = FastAPI()
for route in routes:
    app.include_router(route)

env = dotenv_values(".env")
HOST = environ.get("APP_HOST") if environ.get("APP_HOST") is not None \
    else env["APP_HOST"]
PORT = environ.get("APP_PORT") if environ.get("APP_PORT") is not None \
    else env["APP_PORT"]
if environ.get("APP_RELOAD"):
    RELOAD = environ.get("APP_RELOAD")
elif env["APP_RELOAD"]:
    RELOAD = env["APP_RELOAD"]
else:
    RELOAD = 1

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=HOST,
        port=int(PORT),
        reload=int(RELOAD)
    )
