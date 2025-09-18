from models import db

class Professor(db.Model):
    __tablename__ = "professor"

    # id: chave primária do professor
    id = db.Column(db.Integer, primary_key=True)
    # nome: nome do professor
    nome = db.Column(db.String(100), nullable=False)
    # idade: idade do professor
    idade = db.Column(db.Integer, nullable=False)
    # materia: matéria que o professor leciona
    materia = db.Column(db.String(100), nullable=False)
    # observacoes: informações adicionais sobre o professor
    observacoes = db.Column(db.Text, nullable=True)
    # turmas: relacionamento com a classe Turma, usando back_populates="professor" para criar o vínculo bidirecional
    turmas = db.relationship('Turma', back_populates='professor')

    def __repr__(self):
        return f"<Professor {self.nome} - {self.materia}>"