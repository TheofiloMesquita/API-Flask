from flask import Blueprint, request, jsonify
from models.professor import Professor
from models.base import db

professor_bp = Blueprint("professor", __name__)

@professor_bp.route("/", methods=["POST"])
def post_professor():
    """
    Cria um professor
    ---
    tags:
      - Professores
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [nome, idade, materia]
          properties:
            nome:
              type: string
              example: "Carlos Souza"
            idade:
              type: integer
              example: 40
            materia:
              type: string
              example: "Matemática"
            observacoes:
              type: string
              example: "Professor titular"
    responses:
      201:
        description: Professor criado com sucesso
    """
    data = request.get_json()
    professor = Professor(**data)
    db.session.add(professor)
    db.session.commit()
    return jsonify(professor.to_dict()), 201


@professor_bp.route("/", methods=["GET"])
def get_professores():
    """
    Lista todos os professores
    ---
    tags:
      - Professores
    responses:
      200:
        description: Lista de professores
    """
    professores = Professor.query.all()
    return jsonify([p.to_dict() for p in professores]), 200


@professor_bp.route("/<int:id>", methods=["GET"])
def get_professor(id):
    """
    Obtém um professor pelo ID
    ---
    tags:
      - Professores
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID do professor
    responses:
      200:
        description: Professor encontrado
      404:
        description: Professor não encontrado
    """
    professor = Professor.query.get(id)
    if not professor:
        return jsonify({"error": "Professor não encontrado"}), 404
    return jsonify(professor.to_dict()), 200


@professor_bp.route("/<int:id>", methods=["PUT"])
def put_professor(id):
    """
    Atualiza um professor
    ---
    tags:
      - Professores
    consumes:
      - application/json
    parameters:
      - in: path
        name: id
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            nome:
              type: string
              example: "João Lima"
            idade:
              type: integer
              example: 45
            materia:
              type: string
              example: "Física"
            observacoes:
              type: string
              example: "Substituto"
    responses:
      200:
        description: Professor atualizado
      404:
        description: Professor não encontrado
    """
    professor = Professor.query.get(id)
    if not professor:
        return jsonify({"error": "Professor não encontrado"}), 404

    data = request.get_json()
    for key, value in data.items():
        setattr(professor, key, value)
    db.session.commit()
    return jsonify(professor.to_dict()), 200


@professor_bp.route("/<int:id>", methods=["DELETE"])
def delete_professor(id):
    """
    Exclui um professor
    ---
    tags:
      - Professores
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID do professor
    responses:
      200:
        description: Professor excluído
      404:
        description: Professor não encontrado
    """
    professor = Professor.query.get(id)
    if not professor:
        return jsonify({"error": "Professor não encontrado"}), 404
    db.session.delete(professor)
    db.session.commit()
    return jsonify({"message": "Professor excluído com sucesso"}), 200