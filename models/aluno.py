from models import db

class Aluno(db.Model):
    __tablename__ = "aluno"

    # id: chave primária do aluno
    id = db.Column(db.Integer, primary_key=True)
    # nome: nome do aluno
    nome = db.Column(db.String(100), nullable=False)
    # idade: idade do aluno
    idade = db.Column(db.Integer, nullable=False)
    # turma_id: chave estrangeira que conecta o aluno a uma turma (não nulo)
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)
    # data_nascimento: data de nascimento do aluno
    data_nascimento = db.Column(db.Date, nullable=False)
    # nota_primeiro_semestre: nota do aluno do 1º semestre
    nota_primeiro_semestre = db.Column(db.Float, nullable=True)
    # nota_segundo_semestre: nota do aluno do 2º semestre
    nota_segundo_semestre = db.Column(db.Float, nullable=True)
    # media_final: média final do aluno
    media_final = db.Column(db.Float, nullable=True)
    # turma: relacionamento com a classe Turma, usando back_populates="alunos" para criar o vínculo bidirecional
    turma = db.relationship('Turma', back_populates='alunos')

    def __repr__(self):
        return f"<Aluno {self.nome} - {self.media_final}>"