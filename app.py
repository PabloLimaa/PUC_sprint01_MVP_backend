from flask_openapi3 import OpenAPI, Info, Tag
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
from flask import redirect

from model import Session, Postagem
from schemas import *


info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)


# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
postagem_tag = Tag(name="Postagem", description="Adição, visualização e remoção de postagens na base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/postagem', tags=[postagem_tag],
          responses={"200": PostagemViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_postagem(form: PostagemSchema):
    """Adiciona uma nova Postagem à base de dados

    Retorna uma representação das postagens e comentários associados.
    """
    postagem = Postagem(
        nome=form.nome,
        comentario=form.comentario,
        nota=form.nota)

    try:
        # criando conexão com a base
        session = Session()
        # adicionando postagem
        session.add(postagem)
        # efetivando o camando de adição de nova postagem na tabela
        session.commit()
        return apresenta_postagem(postagem), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Usuário já fez postagem na base :/"
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar nova postagem :/"
        return {"mesage": error_msg}, 400


@app.get('/postagem', tags=[postagem_tag],
         responses={"200": ListagemPostagemSchema, "404": ErrorSchema})
def get_postagens():
    """Faz a busca por todas as postagens efetuadas

    Retorna uma representação da listagem de postagens.
    """
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    postagens = session.query(Postagem).all()

    if not postagens:
        # se não há postagens cadastradas
        return {"postagens": []}, 200
    else:
        # retorna a representação de postagem
        print(postagens)
        return apresenta_postagem(postagens), 200


@app.get('/postagem', tags=[postagem_tag],
         responses={"200": PostagemViewSchema, "404": ErrorSchema})
def get_postagem(query: PostagemBuscaSchema):
    """Faz a busca por uma postagem a partir do id do post

    Retorna uma representação das postagens e comentários associados.
    """
    postagem_id = query.postagem_id
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    postagem = session.query(Postagem).filter(Postagem.id == postagem_id).first()

    if not postagem:
        # se a postagem não foi encontrado
        error_msg = "Postagem não encontrado na base :/"
        return {"mesage": error_msg}, 404
    else:
        # retorna a representação de produto
        return apresenta_postagem(postagem), 200


@app.delete('/postagem', tags=[postagem_tag],
            responses={"200": PostagemDelSchema, "404": ErrorSchema})
def del_postagem(query: PostagemBuscaSchema):
    """Deleta uma postagem a partir do id informado

    Retorna uma mensagem de confirmação da remoção.
    """
    postagem_id = query.postagem_id

    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Postagem).filter(Postagem.id == postagem_id).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        return {"mesage": "Postagem removida", "id": postagem_id}
    else:
        # se a postagem não foi encontrado
        error_msg = "Postagem não encontrado na base :/"
        return {"mesage": error_msg}, 404
