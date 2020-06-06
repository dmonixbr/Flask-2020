from sistema import app, db

ProgramadorTecnologia = db.Table("programadorTecnologia",
                        db.Column('id_programador', db.Integer, db.ForeignKey('programador.id')),
                        db.Column('id_tecnologia', db.Integer, db.ForeignKey('tecnologia.id')))
class Tecnologia(db.Model):
    __tablename__       = "tecnologia"

    id                  = db.Column(db.Integer, primary_key=True)
    nome                = db.Column(db.String(30), nullable=False)
    tipo                = db.Column(db.String(30), nullable=False)
    programadores       = db.relationship("Programador", secondary=ProgramadorTecnologia, back_populates="tecnologias")

