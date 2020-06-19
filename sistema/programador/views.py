import os
from flask import Blueprint, render_template, request, redirect, url_for, current_app
from sistema import db
from sistema.programador.models import Programador
from sistema.tecnologia.models import Tecnologia

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
        avatar = request.files['avatar']

        filename = avatar.filename
        filepath = os.path.join(current_app.root_path, 'static', 'avatares', filename)
        avatar.save(filepath)

        programador = Programador(nome = nome,
                                  experiencia = experiencia,
                                  avatar = filename)
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
        avatar = request.files['avatar']

        filepath_antigo = os.path.join(current_app.root_path, 'static', 'avatares', programador.avatar)
        os.remove(filepath_antigo)

        filename = avatar.filename
        filepath = os.path.join(current_app.root_path, 'static', 'avatares', filename)
        avatar.save(filepath)


        programador.nome = nome
        programador.experiencia = experiencia
        programador.avatar = filename
        
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

@programador.route('/atribuir_tecnologia/<int:_id>', methods=['POST','GET'])
def atribuir_tecnologia(_id):
    programador = Programador.query.get_or_404(_id)
    tecnologias = Tecnologia.query.all()

    if request.method == 'POST':
        id_tecnologia = request.form['id_tecnologia']
        tecnologia = Tecnologia.query.get_or_404(id_tecnologia)
        programador.tecnologias.append(tecnologia)

        db.session.commit()

        return redirect(url_for('programador.index'))
    return render_template('atrubuir_tecnologia.html', programador = programador, tecnologias = tecnologias)

@programador.route('/perfil/<int:_id>')
def perfil(_id):
    programador = Programador.query.get_or_404(_id)

    return render_template('perfil_programador.html', programador = programador)
