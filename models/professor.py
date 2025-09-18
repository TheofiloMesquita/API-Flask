from models import db

class Professor(db.Model):
    __tablename__ = "professor"

    # TODO: Define os campos e o relacionamento da tabela Task
    # - id: chave primária da tarefa
    id = db.Column(db.Integer, primary_key=True)
    # - nome: nome do Professor
    nome = db.Column(db.String(100), nullable=False)
    # - idade: idade do Professor
    idade = db.Column(db.Int, nullable=False)
    # - materia: materia que o Professor leciona
    materia = db.Column(db.String(100), nullable=False)
    # - observacoes: informações adicionais sobre o professor
    observacoes = db.Column(db.Text, nullable=True)
    # - turma: relacionamento com a classe Turma, usando back_populates="professor" para criar o vínculo bidirecional
    turma = db.relationship('Turma', back_populates='professor')

    def __repr__(self):
        return f"<Professor {self.nome} - {self.materia}>"
