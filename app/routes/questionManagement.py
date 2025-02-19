# app/routes/questionManagement.py

from fastapi import APIRouter, Depends, HTTPException
from app.models import SuggestionBaseItem
from app.database import suggestions
from app.auth import authenticate_user

router = APIRouter(prefix="/questions", tags=["Gestión de Preguntas"])

@router.post("", response_model=SuggestionBaseItem)
def add_question(item: SuggestionBaseItem, token_data=Depends(authenticate_user)):
    # Verificar que el usuario tiene rol admin
    if token_data.get("role") != "admin":
        raise HTTPException(status_code=403, detail="No tienes permisos para gestionar las preguntas")
    
    # Se agrega la nueva pregunta y respuesta a la base de conocimiento
    suggestions.append({"pregunta": item.question, "respuesta": item.answer})
    return item
