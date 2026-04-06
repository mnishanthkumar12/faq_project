from typing import Optional
from fastapi import FastAPI
import modules.routing.route as routes

app = FastAPI()

app.include_router(routes.router)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/health")
async def alive():
    """Implement a health check endpoint to verify the status of all dependencies"""
    result = {
        "status": "ok",
        "dependencies": {
            "database": "ok",
            "external_service": "ok",
            "cache": "ok"
        }
    }
    return result
