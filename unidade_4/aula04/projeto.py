from flask import Flask, render_template, request, redirect

from flask_sqlalchemy import SQLAlchemy

# a linha abaixo é a minha variavel de aplicação
app = Flask(__name__)

# a linha abaixo é a configuração do banco
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'admin',
        servidor = 'localhost',
        database = 'aula'
    )

# a linha abaixo instancia o banco de dados
db = SQLAlchemy(app)

# a linha abaixo cria uma classe modelo
class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(200), nullable=False)
    telefone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return "<Name %r>"% self.name

@app.route('/ola')
def mostrar():
    return "<h1>Iniciando aplicação flask</h1>"

@app.route('/lista')
def lista_alunos():

    # a linha abaixo busca os dados na tabela 
    lista = Aluno.query.order_by(Aluno.id)

    return render_template('lista.html', titulo="Listagem de alunos", todos_alunos = lista)


@app.route("/cadastrar")
def cadastrar_aluno():
    return render_template("cadastrar.html")

@app.route("/adicionar", methods=["POST",])
def adicionar_aluno():

    # aqui são as variavei para pegar o que o usuario digitou nos campos
    nome_aluno = request.form['txtNome']
    telefone_aluno = request.form['txtTelefone']
    email_aluno = request.form['txtEmail']

    # instanciando um novo aluno
    novo_aluno = Aluno(nome = nome_aluno, telefone = telefone_aluno, email = email_aluno)

    # a linha abaixo adiciona no banco 
    db.session.add(novo_aluno)

    # grava as mudanças
    db.session.commit()

    return redirect('/lista')



app.run(debug=True)