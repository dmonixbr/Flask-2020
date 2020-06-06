import os
from flask import Flask, render_template, redirect, flash, url_for, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = "qualquercoisameo"

############################################################
################## BANCO DE DADOS ##########################
############################################################


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


#############################################################
####################### BLUEPRINTS ##########################
#############################################################

from sistema.principal.views import principal
from sistema.programador.views import programador
from sistema.tecnologia.views import tecnologia


app.register_blueprint(principal)
app.register_blueprint(programador, url_prefix="/programador")
app.register_blueprint(tecnologia, url_prefix="/tecnologia")
