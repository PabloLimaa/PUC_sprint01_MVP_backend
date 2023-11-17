from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class Postagem(Base):
    __tablename__ = 'postagem'

    id = Column(Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    comentario = Column(String(500))
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, comentario:str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Comentario

        Arguments:
            nome: nome do usuario.
            comentario: comentario sobre o video da pagina
            nota: nota considerada pelo usuario para o MVP
            data_insercao: data de quando o produto foi inserido à base
        """
        self.nome = nome
        self.comentario = comentario

        # se a data não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
