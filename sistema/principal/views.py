from flask import Blueprint, render_template
from sistema.programador.models import Programador
from sistema.tecnologia.models import Tecnologia

principal = Blueprint('principal', __name__)

@principal.route('/')
def index():
    programadores   = Programador.query.all()
    tecnologias     = Tecnologia.query.all()

    return render_template("home.html", programadores=programadores, tecnologias=tecnologias)