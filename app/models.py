from pydantic import BaseModel
from typing import List

class QueryModel(BaseModel):
    queryAsk: str

class SuggestionResponse(BaseModel):
    queryAsk: str
    responseSuggestion: str

class User(BaseModel):
    id: str
    username: str
    password: str
    role: str

class Token(BaseModel):
    sub: str
    idUser: str
    role: str

class  SuggestionBaseItem(BaseModel):
    question: str
    answer: str

class HistoryEntry(BaseModel):
    query: str
    suggestion: str