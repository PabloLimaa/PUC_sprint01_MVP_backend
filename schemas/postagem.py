from pydantic import BaseModel
from typing import Optional, List
from model.postagem import Postagem


class PostagemSchema(BaseModel):
    """ Define como um novo comentario a ser inserido deve ser representado
    """
    nome: str = "Pablo Lima"
    comentario: str = "O vídeo de apresentação do MVP ficou muito legal!"
    nota: Optional[int] = 10
    

class PostagemBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita com base no id da postagem.
    """
    postagem_id: int = 1


class ListagemPostagemSchema(BaseModel):
    """ Define como uma listagem de postagem será retornada.
    """
    postagens:List[PostagemSchema]


def apresenta_postagens(postagens: List[Postagem]):
    """ Retorna uma representação da postagem seguindo o schema definido em
        PostagemViewSchema.
    """
    result = []
    for postagem in postagens:
        result.append({
            "nome": postagem.nome,
            "comentario": postagem.comentario,
            "nota": postagem.nota,
        })

    return {"postagens": result}


class PostagemViewSchema(BaseModel):
    """ Define como uma postagem será retornado: postagem + comentários.
    """
    id: int = 1
    nome: str = "Pablo Lima"
    comentario: str = "O vídeo de apresentação de seu MVP ficou muito legal!"
    nota: Optional[int] = 10
    total_cometarios: int = 1


class PostagemDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_postagem(postagem: Postagem):
    """ Retorna uma representação da postagem seguindo o schema definido em
        PostagemViewSchema.
    """
    return {
        "id": postagem.id,
        "nome": postagem.nome,
        "comentario": postagem.comentario,
        "nota": postagem.nota
    }
