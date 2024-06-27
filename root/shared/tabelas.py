from sqlalchemy import Integer, String, Boolean, Column, Date
from root.shared.database import Base



class Bearer(Base):
    __tablename__ = 'bearer'
    
    id_user = Column(Integer(), primary_key=True, autoincrement=True)
    token = Column(String(), nullable=False)
    nome_user = Column(String(), nullable=False)
    
