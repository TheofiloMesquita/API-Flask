from flask import Blueprint, request, jsonify
from models.aluno import Aluno
from models.base import db
from datetime import datetime

aluno_bp = Blueprint("aluno", __name__)

# ---------------------- CRIAR ----------------------
@aluno_bp.route("/", methods=["POST"])
def create_aluno():
    """
    Cria um aluno
    ---
    tags:
      - Alunos
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - nome
            - idade
            - turma_id
            - data_nascimento
            - nota_primeiro_semestre
            - nota_segundo_semestre
            - media_final
          properties:
            nome:
              type: string
              example: "Ana Clara"
            idade:
              type: integer
              example: 18
            turma_id:
              type: integer
              example: 1
            data_nascimento:
              type: string
              example: "2005-03-12"
            nota_primeiro_semestre:
              type: number
              format: float
              example: 8.0
            nota_segundo_semestre:
              type: number
              format: float
              example: 9.0
            media_final:
              type: number
              format: float
              example: 8.5
    responses:
      201:
        description: Aluno criado com sucesso
      400:
        description: Erro de validação
    """
    data = request.get_json()

    try:
        data_nascimento = datetime.strptime(data["data_nascimento"], "%Y-%m-%d").date()
    except (KeyError, ValueError):
        return jsonify({"error": "Formato de data inválido, use YYYY-MM-DD"}), 400

    aluno = Aluno(
        nome=data["nome"],
        idade=data["idade"],
        turma_id=data["turma_id"],
        data_nascimento=data_nascimento,
        nota_primeiro_semestre=data["nota_primeiro_semestre"],
        nota_segundo_semestre=data["nota_segundo_semestre"],
        media_final=data["media_final"]
    )
    db.session.add(aluno)
    db.session.commit()
    return jsonify({"message": "Aluno criado com sucesso"}), 201


# ---------------------- LISTAR TODOS ----------------------
@aluno_bp.route("/", methods=["GET"])
def get_alunos():
    """
    Lista todos os alunos
    ---
    tags:
      - Alunos
    responses:
      200:
        description: Lista de alunos
    """
    alunos = Aluno.query.all()
    return jsonify([aluno.to_dict() for aluno in alunos]), 200


# ---------------------- LISTAR POR ID ----------------------
@aluno_bp.route("/<int:id>", methods=["GET"])
def get_aluno(id):
    """
    Obtém um aluno por ID
    ---
    tags:
      - Alunos
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do aluno
    responses:
      200:
        description: Aluno encontrado
      404:
        description: Aluno não encontrado
    """
    aluno = Aluno.query.get_or_404(id)
    return jsonify(aluno.to_dict()), 200


# ---------------------- ATUALIZAR ----------------------
@aluno_bp.route("/<int:id>", methods=["PUT"])
def put_aluno(id):
    """
    Atualiza um aluno
    ---
    tags:
      - Alunos
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
              example: "Ana Clara Atualizada"
            idade:
              type: integer
              example: 19
            turma_id:
              type: integer
              example: 1
            data_nascimento:
              type: string
              example: "2004-03-12"
            nota_primeiro_semestre:
              type: number
              example: 7.5
            nota_segundo_semestre:
              type: number
              example: 8.0
            media_final:
              type: number
              example: 7.8
    responses:
      200:
        description: Aluno atualizado
      400:
        description: Erro de validação
    """
    aluno = Aluno.query.get_or_404(id)
    data = request.get_json()

    if "data_nascimento" in data:
        try:
            data["data_nascimento"] = datetime.strptime(
                data["data_nascimento"], "%Y-%m-%d"
            ).date()
        except ValueError:
            return jsonify({"error": "Formato de data inválido, use YYYY-MM-DD"}), 400

    for key, value in data.items():
        if hasattr(aluno, key):
            setattr(aluno, key, value)

    db.session.commit()
    return jsonify(aluno.to_dict()), 200


# ---------------------- DELETAR ----------------------
@aluno_bp.route("/<int:id>", methods=["DELETE"])
def delete_aluno(id):
    """
    Exclui um aluno por ID
    ---
    tags:
      - Alunos
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do aluno
    responses:
      200:
        description: Aluno excluído com sucesso
      404:
        description: Aluno não encontrado
    """
    aluno = Aluno.query.get_or_404(id)
    db.session.delete(aluno)
    db.session.commit()
    return jsonify({"message": "Aluno excluído com sucesso"}), 200