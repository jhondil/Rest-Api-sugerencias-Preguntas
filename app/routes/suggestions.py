# app/routes/suggestions.py

from fastapi import APIRouter, Depends, HTTPException
from app.models import QueryModel, SuggestionResponse
from app.auth import authenticate_user
from app.utils import get_suggestion
from app.database import history

router = APIRouter(prefix="/suggest", tags=["Sugerencias"])

@router.post("", response_model=SuggestionResponse)
def suggest(query: QueryModel, token_data=Depends(authenticate_user)):
   
    if token_data.get("role") != "questionUser":
        raise HTTPException(status_code=403, detail="No tienes permisos para acceder a este endpoint")
    
    suggestion = get_suggestion(query.queryAsk, token_data.get("sub"))
    
    history.append({"query": query.queryAsk, "suggestion": suggestion})
    return {"queryAsk": query.queryAsk, "responseSuggestion": suggestion}
