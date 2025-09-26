from flask import Blueprint, request, jsonify
from models.turma import Turma
from models.base import db

turma_bp = Blueprint("turma", __name__)


@turma_bp.route("/", methods=["POST"])
def create_turma():
    """
    Cria uma turma
    ---
    tags:
      - Turmas
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - descricao
          properties:
            descricao:
              type: string
              example: "Turma A"
            professor_id:
              type: integer
              example: 1
            ativo:
              type: boolean
              example: true
    responses:
      201:
        description: Turma criada com sucesso
      400:
        description: Erro de validação
    """
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Requisição inválida: body JSON obrigatório"}), 400

    descricao = data.get("descricao")
    if not descricao or not isinstance(descricao, str) or not descricao.strip():
        return jsonify({"error": "Campo 'descricao' é obrigatório e deve ser texto"}), 400

    professor_id = data.get("professor_id")
    ativo = data.get("ativo", True)

    turma = Turma(
        descricao=descricao.strip(),
        professor_id=professor_id,
        ativo=bool(ativo)
    )
    db.session.add(turma)
    db.session.commit()

    return jsonify(turma.to_dict()), 201


@turma_bp.route("/", methods=["GET"])
def get_turmas():
    """
    Lista todas as turmas
    ---
    tags:
      - Turmas
    responses:
      200:
        description: Lista de turmas
    """
    turmas = Turma.query.all()
    return jsonify([t.to_dict() for t in turmas]), 200


@turma_bp.route("/<int:id>", methods=["GET"])
def get_turma(id):
    """
    Obtém uma turma por ID
    ---
    tags:
      - Turmas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID da turma
    responses:
      200:
        description: Turma encontrada
      404:
        description: Turma não encontrada
    """
    turma = Turma.query.get_or_404(id)
    return jsonify(turma.to_dict()), 200


@turma_bp.route("/<int:id>", methods=["PUT"])
def put_turma(id):
    """
    Atualiza uma turma
    ---
    tags:
      - Turmas
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
            descricao:
              type: string
              example: "Turma A - Atualizada"
            professor_id:
              type: integer
              example: 2
            ativo:
              type: boolean
              example: false
    responses:
      200:
        description: Turma atualizada
      400:
        description: Erro de validação
      404:
        description: Turma não encontrada
    """
    turma = Turma.query.get_or_404(id)
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Requisição inválida: body JSON obrigatório"}), 400

    if "descricao" in data:
        descricao = data.get("descricao")
        if not descricao or not isinstance(descricao, str) or not descricao.strip():
            return jsonify({"error": "Campo 'descricao' deve ser texto não vazio"}), 400
        turma.descricao = descricao.strip()

    if "professor_id" in data:
        turma.professor_id = data.get("professor_id")

    if "ativo" in data:
        turma.ativo = bool(data.get("ativo"))

    db.session.commit()
    return jsonify(turma.to_dict()), 200


@turma_bp.route("/<int:id>", methods=["DELETE"])
def delete_turma(id):
    """
    Exclui uma turma por ID
    ---
    tags:
      - Turmas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID da turma
    responses:
      200:
        description: Turma excluída com sucesso
      404:
        description: Turma não encontrada
    """
    turma = Turma.query.get_or_404(id)
    db.session.delete(turma)
    db.session.commit()
    return jsonify({"message": "Turma excluída com sucesso"}), 200
