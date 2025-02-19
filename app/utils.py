# app/utils.py

import difflib
from app.database import suggestions

def get_suggestion(user_query: str, username: str) -> str:
    
    preguntas = [item["pregunta"] for item in suggestions]
   
    match = difflib.get_close_matches(user_query, preguntas, n=1, cutoff=0.5)
    if match:
        
        for item in suggestions:
            if item["pregunta"] == match[0]:
                return item["respuesta"]
    return f"Discupa {username}, no tengo una sugerencia para esa consulta."
