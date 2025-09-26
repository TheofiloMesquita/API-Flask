from flask import Flask
from flasgger import Swagger
from models.base import db
from controllers.professor_controller import professor_bp
from controllers.aluno_controller import aluno_bp
from controllers.turma_controller import turma_bp

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SWAGGER"] = {
        "title": "API Escola",
        "uiversion": 3
    }

    db.init_app(app)
    with app.app_context():
        db.create_all()

    Swagger(app)

    # Registrando os blueprints com prefixos
    app.register_blueprint(professor_bp, url_prefix="/professores")
    app.register_blueprint(aluno_bp, url_prefix="/alunos")
    app.register_blueprint(turma_bp, url_prefix="/turmas")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)