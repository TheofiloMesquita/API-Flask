from flask import render_template, request, redirect, url_for
from models.professor import Professor
from models import db

class ProfessorController:

    @staticmethod
    def listar_professores():
        # Busca todos os professores no banco de dados
        professores = Professor.query.all()
        # Renderiza o template com a lista de professores
        return render_template("list_professores.html", professores=professores)
        
    @staticmethod
    def criar_professor():
        if request.method == "POST":
            # Obtém os dados do professor do formulário
            nome = request.form.get("nome")
            idade = request.form.get("idade")
            materia = request.form.get("materia")
            observacoes = request.form.get("observacoes")

            # Conversão de tipos dos dados recebidos
            idade = int(idade) if idade else None
            
            # Cria um novo objeto Professor
            novo_professor = Professor(
                nome=nome,
                idade=idade,
                materia=materia,
                observacoes=observacoes
            )
            # Adiciona e salva o novo professor no banco de dados
            db.session.add(novo_professor)
            db.session.commit()
            # Redireciona para a lista de professores
            return redirect(url_for("ProfessorController.listar_professores"))
        
        # Renderiza o template de criação de professor
        return render_template("create_professor.html")
    
    @staticmethod
    def atualizar_professor(professor_id):
        # Busca o professor pelo ID
        professor = Professor.query.get(professor_id)
        if request.method == "POST" and professor:
            # Obtém os dados atualizados do formulário
            nome = request.form.get("nome")
            idade = request.form.get("idade")
            materia = request.form.get("materia")
            observacoes = request.form.get("observacoes")

            # Conversão de tipos dos dados recebidos
            idade = int(idade) if idade else None

            # Atualiza os campos do professor
            professor.nome = nome
            professor.idade = idade
            professor.materia = materia
            professor.observacoes = observacoes
            db.session.commit()
            # Redireciona para a lista de professores
            return redirect(url_for("ProfessorController.listar_professores"))
        
        # Renderiza o template de atualização de professor com os dados atuais
        return render_template("update_professor.html", professor=professor)

    @staticmethod
    def apagar_professor(professor_id):
        # Busca o professor pelo ID
        professor = Professor.query.get(professor_id)
        if professor:
            try:
                # Tenta deletar o professor do banco de dados
                db.session.delete(professor)
                db.session.commit()
            except Exception as e:
                # Se ocorrer um erro, desfaz a transação e imprime o erro
                db.session.rollback()
                print(f"Erro ao deletar professor: {e}")
        # Redireciona para a lista de professores
        return redirect(url_for("ProfessorController.listar_professores"))