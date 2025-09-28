📚 API Flask - Gerenciamento de Turmas

API desenvolvida em Flask com SQLAlchemy, Flask-Migrate e documentação via Swagger (Flasgger).
O sistema permite gerenciar professores, turmas e alunos, com operações CRUD completas.

✅ Funcionalidades

👨‍🏫 Professores – CRUD completo.

🏫 Turmas – CRUD completo, associadas a professores.

👩‍🎓 Alunos – CRUD completo, associados a turmas.

📑 Swagger – documentação automática disponível em /apidocs.

🔎 Validações – exemplo: não é possível criar aluno sem turma.

🔧 Pré-requisitos

Python 3.11+

Pip

Docker e Docker Compose

Make (opcional, para automação de comandos)

🚀 Como rodar localmente (sem Docker)
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Instale as dependências
pip install -r requirements.txt

# Configure o banco e aplique as migrations
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Rode a aplicação
flask run


➡️ Acesse:

API: http://localhost:5000

Swagger: http://localhost:5000/apidocs

🐳 Como rodar com Docker
# Build dos containers
docker-compose build --no-cache

# Subir API
docker-compose up web


➡️ Acesse:

API: http://localhost:5000

Swagger: http://localhost:5000/apidocs

📦 Makefile (atalhos)

Se você tiver o make instalado:

make build   # Build da aplicação
make up      # Sobe a aplicação
make down    # Para a aplicação
make test    # Roda os testes

🧪 Testes com Pytest

Rodar localmente:

pytest -v


Rodar dentro do Docker:

docker-compose run --rm web pytest -v

📑 Exemplos de uso
Criar Professor
POST /professores
{
  "nome": "João da Silva",
  "email": "joao.silva@escola.com"
}

Criar Turma
POST /turmas
{
  "nome": "Matemática Avançada",
  "professor_id": 1
}

Criar Aluno
POST /alunos
{
  "nome": "Maria Souza",
  "email": "maria.souza@escola.com",
  "data_nascimento": "2005-09-01",
  "turma_id": 1
}

📂 Estrutura do projeto
API-Flask/
│── app.py              # Ponto de entrada Flask
│── config.py           # Configurações da aplicação
│── requirements.txt    # Dependências
│── docker-compose.yml  # Orquestração Docker
│── Dockerfile          # Build da imagem
│── Makefile            # Automação de comandos
│── instance/           # Banco de dados SQLite
│── migrations/         # Controle de versões do banco
│── controllers/        # Rotas (Aluno, Professor, Turma)
│── models/             # Modelos SQLAlchemy
│── tests/              # Testes com pytest

✨ Autor

Projeto desenvolvido para aprendizado de Flask + Swagger + Docker com boas práticas de organização.