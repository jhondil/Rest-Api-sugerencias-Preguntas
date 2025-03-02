
from fastapi import APIRouter, Depends, HTTPException
from app.models import User,ResponseData
from app.auth import authenticate_user
from app.database import users_db
import uuid

router = APIRouter(prefix="/users", tags=["Usuarios"])


@router.post("/register", response_model=ResponseData[User])
def register_user(new_user: User,token_data=Depends(authenticate_user)):
    
    if token_data.get("role") != "admin":
        raise HTTPException(status_code=403, detail="No tienes permisos para gestionar usuarios")

    if new_user.username in users_db:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
 
    user_id = str(uuid.uuid4())
    user = {
        "id": user_id,
        "username": new_user.username,
        "password": new_user.password,  
        "role": new_user.role,
    }
    
    users_db[new_user.username] = user
    
    return ResponseData[User](data=user)


@router.get("")
def get_users(token_data=Depends(authenticate_user)):

    if token_data.get("role") != "admin":
        raise HTTPException(status_code=403, detail="No tienes permisos para gestionar Usuarios")

    return {"data":users_db}

