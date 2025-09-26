from .base import db

class Aluno(db.Model):
    __tablename__ = "alunos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer)
    turma_id = db.Column(db.Integer, db.ForeignKey("turmas.id"), nullable=True)
    data_nascimento = db.Column(db.Date, nullable=True)
    nota_primeiro_semestre = db.Column(db.Float, nullable=True)
    nota_segundo_semestre = db.Column(db.Float, nullable=True)
    media_final = db.Column(db.Float, nullable=True)

    turma = db.relationship("Turma", back_populates="alunos")

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "turma_id": self.turma_id,
            "data_nascimento": self.data_nascimento.isoformat() if self.data_nascimento else None,
            "nota_primeiro_semestre": self.nota_primeiro_semestre,
            "nota_segundo_semestre": self.nota_segundo_semestre,
            "media_final": self.media_final
        }