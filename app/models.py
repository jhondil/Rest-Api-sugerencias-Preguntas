from pydantic import BaseModel
from typing import Generic, TypeVar

DataT = TypeVar('DataT')

class ResponseData(BaseModel, Generic[DataT]):  
    data: DataT  

class QueryModel(BaseModel):
    queryAsk: str

class SuggestionResponse(BaseModel):
    queryAsk: str
    responseSuggestion: str

class User(BaseModel):
    username: str
    password: str
    role: str

class Token(BaseModel):
    sub: str
    idUser: str
    role: str

class LoginRequest(BaseModel):
    username: str
    password: str

class  SuggestionBaseItem(BaseModel):
    question: str
    answer: str

class HistoryEntry(BaseModel):
    query: str
    suggestion: str


