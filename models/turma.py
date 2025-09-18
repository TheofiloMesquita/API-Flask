from models import db

class Turma(db.Model):
    __tablename__ = "turma"

    # TODO: Define os campos e o relacionamento da tabela Turma
    # - id: chave primária da tarefa
    id = db.Column(db.Integer, primary_key=True)
    # - description: nome ou descrição da turma
    description = db.Column(db.String(100), nullable=True)
    # - professor_id: chave estrangeira que conecta a turma a um professor (não nulo)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    # - ativo: indica se a turma está ativa
    ativo = db.Column(db.Boolean, nullable=False)
    # - professor: relacionamento com a classe Professor, usando back_populates="turma" para criar o vínculo bidirecional
    professor = db.relationship('Professor', back_populates='turma')

    def __repr__(self):
        return f"<Turma {self.description} - {self.ativo}>"
