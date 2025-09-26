from .base import db

class Turma(db.Model):
    __tablename__ = "turmas"
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey("professores.id"), nullable=True)
    ativo = db.Column(db.Boolean, default=True)

    professor = db.relationship("Professor", back_populates="turmas")
    alunos = db.relationship("Aluno", back_populates="turma", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "descricao": self.descricao,
            "professor_id": self.professor_id,
            "ativo": self.ativo
        }