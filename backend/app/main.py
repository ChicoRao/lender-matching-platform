from fastapi import FastAPI
from fastapi.routing import APIRoute

from app.api.routes import applications

app = FastAPI()

# Set CORS

# Set Router
app.include_router(applications.router, prefix="/v1/applications")