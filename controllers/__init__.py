# controllers/__init__.py
from .professor_controller import professor_bp
from .turma_controller import turma_bp
from .aluno_controller import aluno_bp

__all__ = ["professor_bp", "turma_bp", "aluno_bp"]
