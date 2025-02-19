
from fastapi import APIRouter, Depends, HTTPException
from app.models import QueryModel, SuggestionResponse,ResponseData  
from app.auth import authenticate_user
from app.utils import get_suggestion
from app.database import history

router = APIRouter(prefix="/suggest", tags=["Sugerencias"])

@router.post("", response_model=ResponseData[SuggestionResponse])
def suggest(query: QueryModel, token_data=Depends(authenticate_user)):
   
    if token_data.get("role") != "questionUser":
        raise HTTPException(status_code=403, detail="No tienes permisos para acceder a este endpoint")
    
    suggestion_text = get_suggestion(query.queryAsk, token_data.get("sub"))
    
    suggestion = SuggestionResponse(queryAsk=query.queryAsk, responseSuggestion=suggestion_text)
    
    history.append({"query": query.queryAsk, "suggestion": suggestion_text})
    
    return ResponseData[SuggestionResponse](data=suggestion)
