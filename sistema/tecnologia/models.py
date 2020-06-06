from sistema import app, db

class Tecnologia(db.Model):
    __tablename__       = "tecnologia"

    id                  = db.Column(db.Integer, primary_key=True)
    nome                = db.Column(db.String(30), nullable=False)
    tipo                = db.Column(db.String(30), nullable=False)
    programadores       = db.relationship("Programador", secundary=ProgramadorTecnologia, back_populates="tecnologias")

ProgramadorTecnologia = db.Table("ProgramadorTecnologia",
                        db.Column('id_programador', db.Integer, db.ForeignKey('programador.id')),
                        db.Column('id_tecnologia', db.Integer, db.ForeignKey('tecnologia.id')))