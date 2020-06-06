from flask import Blueprint, render_template

tecnologia = Blueprint('tecnologia', __name__, template_folder="templates")

@tecnologia.route('/')
def index():
    return render_template('programadores.html')