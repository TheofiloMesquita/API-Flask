from flask import Flask, jsonify
from flasgger import Swagger
from models.base import db
from config import Config

# Importar blueprints
from controllers.aluno_controller import aluno_bp
from controllers.professor_controller import professor_bp
from controllers.turma_controller import turma_bp


def create_app():
    """Factory para criar a aplicação Flask"""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensões
    db.init_app(app)
    Swagger(app)

    # Criar tabelas se não existirem
    with app.app_context():
        db.create_all()

    # Registrar blueprints
    app.register_blueprint(aluno_bp, url_prefix="/alunos")
    app.register_blueprint(professor_bp, url_prefix="/professores")
    app.register_blueprint(turma_bp, url_prefix="/turmas")

    # Rota de saúde
    @app.route("/")
    def index():
        return jsonify({"message": "API de Gestão Escolar rodando com Flask + Swagger!"})

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)