from sistema import app, db
from sistema.tecnologia.models import ProgramadorTecnologia

class Programador(db.Model):
    __tablename__       = "programador"

    id                  = db.Column(db.Integer, primary_key=True)
    nome                = db.Column(db.String(30), nullable=False)
    experiencia         = db.Column(db.Integer, nullable=False)
    tecnologias         = db.relationship("Tecnologia", secundary=ProgramadorTecnologia, back_populates="programadores")