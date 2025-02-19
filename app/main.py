from typing import Union
from app.auth import router  as auth_router
from app.routes.suggestions import router  as suggestions_router
from app.routes.historyChat import router  as historyChat_router
from app.routes.questionManagement import router  as question_management
from app.routes.users import router  as users

from fastapi import FastAPI

def create_app():
    app = FastAPI(title="Rest Api sugerencias Preguntas")
    app.include_router(auth_router)
    app.include_router(suggestions_router)
    app.include_router(historyChat_router)
    app.include_router(question_management)
    app.include_router(users)

    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)