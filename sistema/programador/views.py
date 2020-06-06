from flask import Blueprint, render_template, request, redirect, url_for
from sistema import db
from sistema.programador.models import Programador

programador = Blueprint('programador', __name__, template_folder="templates")

@programador.route('/')
def index():
    programadores = Programador.query.all()
    return render_template('index.html', programadores = programadores)

@programador.route('/cadastrar', methods=['POST','GET'])
def cadastrar():
    if request.method == "POST":
        nome = request.form['nome']
        experiencia = request.form['exp']

        programador = Programador(nome = nome,
                                  experiencia = experiencia)
        db.session.add(programador)
        db.session.commit()

        return redirect(url_for('programador.index'))
    return render_template('cadastrar_programador.html')

@programador.route('/editar/<int:_id>', methods=['GET','POST'])
def editar_programador(_id):
    programador = Programador.query.get_or_404(_id)

    if request.method == 'POST':
        nome = request.form['nome']
        experiencia = request.form['exp']

        programador.nome = nome
        programador.experiencia = experiencia

        db.session.commit()

        return redirect(url_for('programador.index'))

    return render_template('editar_programador.html', programador = programador)

@programador.route('/excluir/<int:_id>', methods=['POST','GET'])
def excluir_programador(_id):
    programador = Programador.query.get_or_404(_id)

    if request.method == 'POST':
        db.session.delete(programador)
        db.session.commit()

        return redirect(url_for('programador.index'))

    return render_template('excluir_programador.html', programador = programador)