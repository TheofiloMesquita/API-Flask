# 📚 API Flask - Gerenciamento Turmas

Projeto desenvolvido em **Flask** seguindo o padrão **MVC (Model-View-Controller)**, utilizando **SQLAlchemy** para persistência de dados, **Flask-Migrate** para migrations e documentação com **Swagger (Flasgger)**.

O sistema permite gerenciar **professores**, **turmas** e **alunos**, incluindo operações **CRUD** completas e validação de relacionamentos:
- Um professor pode ter várias turmas.
- Uma turma pertence a um professor e pode ter vários alunos.
- Um aluno pertence a uma turma.

---

## 🚀 Tecnologias utilizadas
- [Flask](https://flask.palletsprojects.com/)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Marshmallow](https://marshmallow.readthedocs.io/)
- [Flasgger (Swagger UI)](https://github.com/flasgger/flasgger)
- [Docker](https://www.docker.com/)

---

## 🏗 Arquitetura MVC
O projeto segue a estrutura **MVC**:


/project
├── app.py # Arquivo principal da aplicação
├── models/ # Modelos do banco (ORM SQLAlchemy)
│ ├── professor.py
│ ├── turma.py
│ └── aluno.py
├── controllers/ # Regras de negócio e rotas
│ ├── professor_controller.py
│ ├── turma_controller.py
│ └── aluno_controller.py
├── utils/ # Schemas do Marshmallow
│ └── schemas.py
├── migrations/ # Arquivos de controle do Flask-Migrate
├── swagger_template.yml # Definições do Swagger
├── Dockerfile
└── docker-compose.yml


---

## ⚙️ Como rodar localmente

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo

2. Crie um ambiente virtual e instale dependências
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt

3. Configure o banco de dados (SQLite por padrão)
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

4. Rode a aplicação
flask run


➡️ Acesse no navegador:

API: http://localhost:5000/

Swagger: http://localhost:5000/apidocs

🐳 Como rodar com Docker
docker-compose up --build


➡️ Acesse:

API: http://localhost:5000/

Swagger: http://localhost:5000/apidocs

🔗 Endpoints da API
Professores

GET /professores/ → lista professores

GET /professores/{id} → busca professor por ID

POST /professores/ → cria professor

PUT /professores/{id} → atualiza professor

DELETE /professores/{id} → remove professor

📌 Exemplo de criação (POST /professores/):

{
  "nome": "João da Silva",
  "idade": 40,
  "materia": "Matemática",
  "observacoes": "Professor titular"
}

Turmas

GET /turmas/ → lista turmas

GET /turmas/{id} → busca turma por ID

POST /turmas/ → cria turma (precisa de professor_id válido)

PUT /turmas/{id} → atualiza turma

DELETE /turmas/{id} → remove turma

📌 Exemplo de criação (POST /turmas/):

{
  "descricao": "Turma de Engenharia Civil - 1º semestre",
  "professor_id": 1,
  "ativo": true
}

Alunos

GET /alunos/ → lista alunos

GET /alunos/{id} → busca aluno por ID

POST /alunos/ → cria aluno (precisa de turma_id válido)

PUT /alunos/{id} → atualiza aluno

DELETE /alunos/{id} → remove aluno

📌 Exemplo de criação (POST /alunos/):

{
  "nome": "Ana Souza",
  "idade": 20,
  "turma_id": 1,
  "data_nascimento": "2005-05-10",
  "nota_primeiro_semestre": 8.5,
  "nota_segundo_semestre": 7.0
}

✅ Validações extras

Não é possível criar Turma sem professor existente.

Não é possível criar Aluno sem turma existente.

IDs são gerados automaticamente (não devem ser enviados no POST).

🖥 Swagger UI

Toda a documentação interativa está disponível em:
👉 http://localhost:5000/apidocs

No Swagger, os exemplos já estão preenchidos automaticamente (example) para facilitar os testes.

👨‍💻 Autor

Projeto desenvolvido para fins acadêmicos e de aprendizado em Flask + SQLAlchemy + Swagger.

---