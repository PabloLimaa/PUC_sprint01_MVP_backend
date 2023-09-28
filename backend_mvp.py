from flask import Flask, render_template, request, redirect, session, flash, url_for

# definindo uma class para os comentários____________
class Comentarios:
    def __init__(self, nome, comentario):
        self.nome = nome
        self.comentario = comentario

comentario01 = Comentarios('Pablo Lima', 'Ficou bem interessante seu MVP!')
comentario02 = Comentarios('Yago Vinicius', 'Ficou bem interessante seu MVP!')

lista_comentarios = [comentario01, comentario02]

# inicializando o flask em uma variável app_________________________
app = Flask(__name__)
app.secret_key = 'pablo'

# rota HOME_____________________________
@app.route('/index',  methods=['POST','GET'])
@app.route('/',  methods=['POST','GET'])
def home():
    return render_template('index.html', titulo='Deixe seu Comentário', lista_comentarios=lista_comentarios)

# rota CRIAR______________________________
@app.route('/criar',  methods=['POST','GET'])
def criar():
    nome = request.form['nome']
    comentario = request.form['comentario']

    postagem = Comentarios(nome, comentario)
    lista_comentarios.append(postagem)

    return redirect(url_for('home'))

#####################################################
# rota DELETAR_______________________________
@app.route('/deletar',  methods=['POST','DELETE','GET'])
def deletar():
    return redirect(url_for('home'))

# para manter a página atualizando automaticamente____________________
if __name__ == "__main__":
    app.run(debug=True)
