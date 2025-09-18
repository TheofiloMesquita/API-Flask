from flask import render_template, request, redirect, url_for
from models.turma import Turma
from models.professor import Professor
from models import db

class TurmaController:

    @staticmethod
    def listar_turmas():
        # Busca todas as turmas no banco de dados
        turmas = Turma.query.all()
        # Renderiza o template com a lista de turmas
        return render_template("list_turmas.html", turmas=turmas)
    
    @staticmethod
    def criar_turma():
        if request.method == "POST":
            # Obtém os dados do formulário
            descricao = request.form.get("descricao")
            professor_id = request.form.get("professor_id")
            ativo = request.form.get("ativo") == "on"

            # Verifica se o professor existe
            professor = Professor.query.get(professor_id)
            if not professor:
                return "Erro: Professor não encontrado", 400

            # Cria um novo objeto Turma
            nova_turma = Turma(
                descricao=descricao,
                professor=professor,
                ativo=ativo
            )
            # Adiciona e salva a nova turma no banco de dados
            db.session.add(nova_turma)
            db.session.commit()
            # Redireciona para a lista de turmas
            return redirect(url_for("TurmaController.listar_turmas"))
        
        # Busca todos os professores para exibir no formulário
        professores = Professor.query.all()
        # Renderiza o template de criação de turma
        return render_template("create_turma.html", professores=professores)
    
    @staticmethod
    def atualizar_turma(turma_id):
        # Busca a turma pelo ID
        turma = Turma.query.get(turma_id)
        if request.method == "POST" and turma:
            # Obtém os dados do formulário
            descricao = request.form.get("descricao")
            professor_id = request.form.get("professor_id")
            ativo = request.form.get("ativo") == "on"

            # Verifica se o professor existe
            professor = Professor.query.get(professor_id)
            if not professor:
                return "Erro: Professor não encontrado", 400

            # Atualiza os campos da turma
            turma.descricao = descricao
            turma.professor = professor
            turma.ativo = ativo
            db.session.commit()
            # Redireciona para a lista de turmas
            return redirect(url_for("TurmaController.listar_turmas"))

        # Busca todos os professores para exibir no formulário de edição
        professores = Professor.query.all()
        # Renderiza o template de edição de turma
        return render_template("edit_turma.html", turma=turma, professores=professores)

    @staticmethod
    def apagar_turma(turma_id):
        # Busca a turma pelo ID
        turma = Turma.query.get(turma_id)
        # Remove a turma do banco de dados, se existir
        if turma:
            db.session.delete(turma)
            db.session.commit()
        # Redireciona para a lista de turmas
        return redirect(url_for("TurmaController.listar_turmas"))