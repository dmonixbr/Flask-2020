from flask import Blueprint, render_template

programador = Blueprint('programador', __name__, template_folder="templates")

@programador.route('/')
def index():
    return render_template('index.html')