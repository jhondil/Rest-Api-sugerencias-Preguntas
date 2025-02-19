from fastapi import FastAPI, Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
import datetime
from app.models import QueryModel
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

SECRET_KEY = os.getenv("SECRET_KEY")
scheme_oauth2 = OAuth2PasswordBearer(tokenUrl="token")

users_db = {
    "user": {
        "id":"8aa1a5f6-680e-435d-9367-ef57bdaca5b8",
        "username": "userQuestion",
        "password": "Password123!",
        "role": "questionUser",
    },
    "admin": {"id":"8cfd3a42-729d-493a-b38f-fea89f003d74","username": "admin", "password": "PasswordAdmin", "role": "admin"},
}


def authenticate_user(token: str = Depends(scheme_oauth2)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user or user["password"] != form_data.password:
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")
    token = jwt.encode(
        {
            "sub": form_data.username,
            "role": user["role"],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        },
        SECRET_KEY,
        algorithm="HS256",
    )
    return {"access_token": token, "token_type": "bearer"}
