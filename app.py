from flask import Flask, redirect, url_for, render_template, request

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cliente.db'
# app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:root@localhost:5432/DBImpacta'

db = SQLAlchemy(app)


class Aluno(db.Model):  # herdando da classe db.Model que gera a tabela
    __tablename__ = 'alunoNoemi'
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
    return redirect(url_for('alunos'))


@app.route('/alunos')
def alunos():
    alunos = Aluno.query.all()
    return render_template('alunos/alunos-list.html', alunos=alunos)


@app.route('/alunos/create', methods=['GET','POST'])
def alunos_create():
    if request.method == 'POST':
        aluno = Aluno(  request.form['nome'], 
                        request.form['email'],
                        request.form['cep'], 
                        request.form['logradouro'],
                        request.form['numero'], 
                        request.form['bairro'])

        db.session.add(aluno)
        db.session.commit()

        return redirect(url_for('alunos'))

    return render_template('alunos/alunos-create.html')


@app.route('/alunos/edit/<int:id>', methods=['GET','POST'])
def alunos_edit(id):
    aluno = Aluno.query.get(id)
    if request.method == 'POST':
        aluno.nome = request.form['nome']
        aluno.email = request.form['email']
        aluno.cep = request.form['cep']
        aluno.logradouro = request.form['logradouro']
        aluno.numero = request.form['numero']
        aluno.bairro = request.form['bairro']
        db.session.commit()
        return redirect(url_for('alunos'))
        
    return render_template('alunos/alunos-edit.html', aluno=aluno)


@app.route('/alunos/delete/<int:id>')
def alunos_delete(id):
    aluno = Aluno.query.get(id)
    db.session.delete(aluno)
    db.session.commit()
    return redirect(url_for('alunos'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
