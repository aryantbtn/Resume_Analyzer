from fastapi import FastAPI

from app.api.auth_routes import router as auth_router

from app.api.resume_routes import (
    router as resume_router
)

app = FastAPI(
    title="AI Resume Analyzer"
)

app.include_router(
    auth_router
)

app.include_router(
    resume_router
)

@app.get("/")
def home():

    return {
        "message":
        "AI Resume Analyzer Running"
    }