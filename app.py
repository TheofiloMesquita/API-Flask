import os
from flask import Flask
from config import Config
from controllers.aluno_controller import AlunoController
from controllers.professor_controller import ProfessorController
from controllers.turma_controller import TurmaController
from models.aluno import Aluno
from models.professor import Professor
from models.turma import Turma
from models import db

app = Flask(__name__, template_folder=os.path.join('view', 'templates'))
app.config.from_object(Config)

# inicializa o banco de dados
db.init_app(app)

# cria tabelas
with app.app_context():
    db.create_all()

# forma alternativa de criar rotas, parâmetros: rota em si, endpoint interno do flask e função a ser executada quando a URL for acessada

# Rotas Alunos
app.add_url_rule("/alunos", view_func=AlunoController.listar_Alunos, endpoint="listar_Alunos")
app.add_url_rule("/alunos/new", view_func=AlunoController.criar_aluno, methods=["GET", "POST"], endpoint="criar_aluno")
app.add_url_rule("/alunos/update/<int:aluno_id>", view_func=AlunoController.atualizar_aluno, methods=["GET", "POST"], endpoint="atualizar_dados_aluno")
app.add_url_rule("/alunos/delete/<int:aluno_id>", view_func=AlunoController.apagar_aluno, methods=["POST"], endpoint="delete_aluno")

# Rotas Professores
app.add_url_rule("/professores", view_func=ProfessorController.listar_professores, endpoint="listar_professores")
app.add_url_rule("/professores/new", view_func=ProfessorController.criar_professor, methods=["GET", "POST"], endpoint="criar_professor")
app.add_url_rule("/professores/update/<int:professor_id>", view_func=ProfessorController.atualizar_professor, methods=["GET", "POST"], endpoint="atualizar_dados_professor")
app.add_url_rule("/professores/delete/<int:professor_id>", view_func=ProfessorController.apagar_professor, methods=["POST"], endpoint="delete_professor")

# Rotas Turmas
app.add_url_rule("/turmas", view_func=TurmaController.listar_turmas, endpoint="listar_turmas")
app.add_url_rule("/turmas/new", view_func=TurmaController.criar_turma, methods=["GET", "POST"], endpoint="criar_turma")
app.add_url_rule("/turmas/update/<int:turma_id>", view_func=TurmaController.atualizar_turma, methods=["GET", "POST"], endpoint="atualizar_dados_turma")
app.add_url_rule("/turmas/delete/<int:turma_id>", view_func=TurmaController.apagar_turma, methods=["POST"], endpoint="delete_turma")

if __name__ == '__main__':
    app.run(debug=True, port=5002)
