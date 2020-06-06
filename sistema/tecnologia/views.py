from flask import Blueprint, render_template, request, redirect, url_for
from sistema import db
from sistema.tecnologia.models import Tecnologia

tecnologia = Blueprint('tecnologia', __name__, template_folder="templates")

@tecnologia.route('/')
def index():
    tecnologias = Tecnologia.query.all()
    return render_template('tecnologias.html', tecnologias = tecnologias)

@tecnologia.route('/cadastrar', methods=['POST','GET'])
def cadastrar():
    if request.method == "POST":
        nome = request.form['nome']
        tipo = request.form['tipo']

        tecnologia = Tecnologia(nome = nome,
                                  tipo = tipo)
        db.session.add(tecnologia)
        db.session.commit()

        return redirect(url_for('tecnologia.index'))
    return render_template('cadastrar_tecnologia.html')

@tecnologia.route('/editar/<int:_id>', methods=['POST','GET'])
def editar_tecnologia(_id):
    tecnologia = Tecnologia.query.get_or_404(_id)

    if request.method == 'POST':
        nome = request.form['nome']
        tipo = request.form['tipo']

        tecnologia.nome = nome
        tecnologia.tipo = tipo

        db.session.commit()

        return redirect(url_for('tecnologia.index'))

    return render_template('editar_tecnologia.html', tecnologia = tecnologia)

@tecnologia.route('/excluir/<int:_id>', methods=['POST','GET'])
def excluir_tecnologia(_id):
    tecnologia = Tecnologia.query.get_or_404(_id)

    if request.method == 'POST':
        db.session.delete(tecnologia)
        db.session.commit()

        return redirect(url_for('tecnologia.index'))

    return render_template('excluir_tecnologia.html', tecnologia = tecnologia)

@tecnologia.route('/perfil/<int:_id>')
def perfil(_id):
    tecnologia = Tecnologia.query.get_or_404(_id)

    return render_template('perfil_tecnologia.html', tecnologia = tecnologia)