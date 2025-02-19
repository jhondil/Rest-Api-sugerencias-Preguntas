from typing import Union
from app.auth import router  as auth_router

from fastapi import FastAPI

def create_app():
    app = FastAPI(title="Rest Api sugerencias Preguntas")
    app.include_router(auth_router)
    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)