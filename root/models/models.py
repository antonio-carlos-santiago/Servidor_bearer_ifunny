from pydantic import BaseModel
from typing import List


class Clientes(BaseModel):
    status: bool = True
    data: dict
    
    
class Importacao(BaseModel):
    data: List = [
        {
        'token': 'Bearer casjkjkcsjakcacaskcjsalascjascjaslkclsakcksacas',
        'nome_user': 'Sara'
        }
    ]
    
    
class ResponseModel(BaseModel):
    status: bool = True
    message: dict