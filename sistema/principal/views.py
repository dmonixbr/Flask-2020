from flask import Blueprint

principal = Blueprint('principal', __name__)

@principal.route('/')
def index():

    return "oi"