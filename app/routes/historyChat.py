
from fastapi import APIRouter, Depends, HTTPException
from app.database import history
from app.auth import authenticate_user

router = APIRouter(prefix="/history", tags=["Historial"])

@router.get("")
def get_history(token_data=Depends(authenticate_user)):    
    
    return {"data":history}
