from models import db

class Aluno(db.Model):
    __tablename__ = "aluno"

    # TODO: Define os campos e o relacionamento da tabela Task
    # - id: chave primária da tarefa
    id = db.Column(db.Integer, primary_key=True)
    # - nome: nome do aluno
    nome = db.Column(db.String(100), nullable=False)
    # - idade: idade do aluno
    idade = db.Column(db.Int, nullable=False)
    # - turma_id: chave estrangeira que conecta a turma a um aluno (não nulo)
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)
    # - data_nascimento: data de nascimento do aluno
    data_nascimento = db.Column(db.Date, default="Pendente", nullable=False)
    # - nota_primeiro_semestre: nota do aluno do 1º semestre
    nota_primeiro_semestre = db.Column(db.Float, nullable=True)
    # - nota_segundo_semestre: nota do aluno do 2º semestre
    nota_segundo_semestre = db.Column(db.Float, nullable=True)
    # - media_final: média final do aluno
    media_final = db.Column(db.Float, nullable=True)
    # - user: relacionamento com a classe Turma, usando back_populates="aluno" para criar o vínculo bidirecional
    user = db.relationship('Turma', back_populates='aluno')

    def __repr__(self):
        return f"<Aluno {self.nome} - {self.media_final}>"
