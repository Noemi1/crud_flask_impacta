from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cliente.db"
# app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql://postgres:root@localhost:5432/DBImpacta"

db = SQLAlchemy(app)


class Aluno(db.Model):  # herdando da classe db.Model que gera a tabela
    __tablename__ = 'alunoHenrique'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(50))
    cep = db.Column(db.String(10))
    logradouro = db.Column(db.String(50))
    numero = db.Column(db.String(10))
    bairro = db.Column(db.String(50))

    def __init__(self, nome, email, cep, logradouro, numero, bairro):
        self.nome = nome
        self.email = email
        self.cep = cep
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro


@app.route('/')
def index():
    alunos = Aluno.query.all()
    return render_template("index.html", alunos=alunos)



@app.route("/add", methods=['GET','POST'])
def add():
    if request.method == 'POST':
        aluno = Aluno(request.form['nome'], request.form['email'],
                      request.form['cep'], request.form['logradouro',
                      request.form['numero'], request.form['bairro'])
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

'''

@app.route("/edit/<int:id>", methods=['GET','POST'])
def edit(id):
    cliente = Cliente.query.get(id)
    if request.method == 'POST':
        cliente.name = request.form['nome']
        cliente.comment = request.form['comentario']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', cliente=cliente)

@app.route("/delete/<int:id>")
def delete(id):
    cliente = Cliente.query.get(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('index'))
'''

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
