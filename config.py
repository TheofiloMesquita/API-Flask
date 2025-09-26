import os

# Caminho base do projeto
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Chave secreta usada por Flask (sessões, segurança)
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret")

    # Banco de dados SQLite dentro da pasta instance/
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(basedir, "instance", "app.db")
    )

    # Desativa notificações de modificação para economizar recursos
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuração do Swagger (documentação da API)
    SWAGGER = {
        "title": "API Professores/Turmas/Alunos",
        "uiversion": 3
    }