from fastapi import APIRouter, Depends, HTTPException
from root.shared.dependencies import get_db
from root.shared.tabelas import Bearer
from sqlalchemy.orm import Session
from root.models.models import Clientes, Importacao, ResponseModel



routes_users = APIRouter(prefix='/bearer', tags=['Bearer'])


@routes_users.get(path='/users', response_model=Clientes)
def tokens(db: Session = Depends(get_db)):
    clientes_dict = {}
    codigos_bearer =  db.query(Bearer).all()
    for clientes in codigos_bearer:
        clientes_dict[clientes.nome_user] = clientes.token
        
    return {'data': clientes_dict}


@routes_users.post(path='/importacao', response_model=ResponseModel)
def importacao(data_user: Importacao, db: Session = Depends(get_db)):
    for cliente in data_user.data:
        new_cliente = Bearer(
            token=cliente['token'],
            nome_user=cliente['nome_user']
        )
        
        db.add(new_cliente)
        db.commit()
        db.refresh(new_cliente)
        
    return {'message': {"message": 'clientes importados com sucesso'}}