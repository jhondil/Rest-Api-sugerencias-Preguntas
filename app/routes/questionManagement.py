from fastapi import APIRouter, Depends, HTTPException
from app.models import SuggestionBaseItem,ResponseData
from app.database import suggestions
from app.auth import authenticate_user

router = APIRouter(prefix="/questions", tags=["Gestión de Preguntas"])

@router.post("", response_model=ResponseData[SuggestionBaseItem])
def add_question(item: SuggestionBaseItem, token_data=Depends(authenticate_user)):
   
    if token_data.get("role") != "admin":
        raise HTTPException(status_code=403, detail="No tienes permisos para gestionar las preguntas")
    
   
    suggestions.append({"pregunta": item.question, "respuesta": item.answer})
    return ResponseData[SuggestionBaseItem](data=item)
    
