from flask import render_template, request, redirect, url_for
from models.aluno import Aluno
from models.turma import Turma
from models.professor import Professor
from models import db
import datetime

class AlunoController:

    @staticmethod
    def listar_Alunos():
        # Busca todos os alunos no banco de dados
        alunos = Aluno.query.all()
        # Renderiza o template com a lista de alunos
        return render_template("list_alunos.html", alunos=alunos)
    
    @staticmethod
    def criar_aluno():
        if request.method == "POST":
            # Obtém os dados do formulário
            nome = request.form.get("nome")
            idade = request.form.get("idade")
            turma_id = request.form.get("turma_id")
            data_nascimento = request.form.get("data_nascimento")
            nota_primeiro_semestre = request.form.get("nota_primeiro_semestre")
            nota_segundo_semestre = request.form.get("nota_segundo_semestre")

            # Conversão de tipos dos dados recebidos
            idade = int(idade) if idade else None
            turma_id = int(turma_id) if turma_id else None
            try:
                data_nascimento = datetime.datetime.strptime(data_nascimento, "%Y-%m-%d").date()
            except Exception:
                data_nascimento = None
            nota_primeiro_semestre = float(nota_primeiro_semestre) if nota_primeiro_semestre else None
            nota_segundo_semestre = float(nota_segundo_semestre) if nota_segundo_semestre else None
            # Calcula a média final se ambas as notas estiverem presentes
            media_final = (nota_primeiro_semestre + nota_segundo_semestre) / 2 if nota_primeiro_semestre is not None and nota_segundo_semestre is not None else None

            # Cria um novo objeto Aluno
            novo_aluno = Aluno(
                nome=nome,
                idade=idade,
                turma_id=turma_id,
                data_nascimento=data_nascimento,
                nota_primeiro_semestre=nota_primeiro_semestre,
                nota_segundo_semestre=nota_segundo_semestre,
                media_final=media_final
            )
            # Adiciona e salva o novo aluno no banco de dados
            db.session.add(novo_aluno)
            db.session.commit()
            # Redireciona para a lista de alunos
            return redirect(url_for("AlunoController.listar_Alunos"))

        # Busca todas as turmas e professores para exibir no formulário
        turmas = Turma.query.all()
        professores = Professor.query.all()
        # Renderiza o template de criação de aluno
        return render_template("create_aluno.html", turmas=turmas, professores=professores)

    @staticmethod
    def atualizar_aluno(aluno_id):
        # Busca o aluno pelo ID
        aluno = Aluno.query.get(aluno_id)
        if request.method == "POST":
            # Obtém os dados do formulário
            nome = request.form.get("nome")
            idade = request.form.get("idade")
            turma_id = request.form.get("turma_id")
            data_nascimento = request.form.get("data_nascimento")
            nota_primeiro_semestre = request.form.get("nota_primeiro_semestre")
            nota_segundo_semestre = request.form.get("nota_segundo_semestre")

            # Conversão de tipos dos dados recebidos
            idade = int(idade) if idade else None
            turma_id = int(turma_id) if turma_id else None
            try:
                data_nascimento = datetime.datetime.strptime(data_nascimento, "%Y-%m-%d").date()
            except Exception:
                data_nascimento = None
            nota_primeiro_semestre = float(nota_primeiro_semestre) if nota_primeiro_semestre else None
            nota_segundo_semestre = float(nota_segundo_semestre) if nota_segundo_semestre else None
            # Calcula a média final se ambas as notas estiverem presentes
            media_final = (nota_primeiro_semestre + nota_segundo_semestre) / 2 if nota_primeiro_semestre is not None and nota_segundo_semestre is not None else None

            # Atualiza os dados do aluno
            if aluno:
                aluno.nome = nome
                aluno.idade = idade
                aluno.turma_id = turma_id
                aluno.data_nascimento = data_nascimento
                aluno.nota_primeiro_semestre = nota_primeiro_semestre
                aluno.nota_segundo_semestre = nota_segundo_semestre
                aluno.media_final = media_final
                db.session.commit()
            # Redireciona para a lista de alunos
            return redirect(url_for("AlunoController.listar_Alunos"))

        # Busca todas as turmas e professores para exibir no formulário de edição
        turmas = Turma.query.all()
        professores = Professor.query.all()
        # Renderiza o template de edição de aluno
        return render_template("edit_aluno.html", aluno=aluno, turmas=turmas, professores=professores)

    @staticmethod
    def apagar_aluno(aluno_id):
        # Busca o aluno pelo ID
        aluno = Aluno.query.get(aluno_id)
        # Remove o aluno do banco de dados, se existir
        if aluno:
            db.session.delete(aluno)
            db.session.commit()
        # Redireciona para a lista de alunos
        return redirect(url_for("AlunoController.listar_Alunos"))