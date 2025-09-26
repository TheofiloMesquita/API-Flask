import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import create_app, db
from models.aluno import Aluno
from models.professor import Professor
from models.turma import Turma

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()


# ---------- PROFESSORES ----------
def test_crud_professor(client):
    res = client.post("/professores/", json={
        "nome": "Carlos Souza",
        "idade": 40,
        "materia": "Matemática",
        "observacoes": "Titular"
    })
    assert res.status_code == 201
    prof_id = res.get_json()["id"]

    res = client.get(f"/professores/{prof_id}")
    assert res.status_code == 200

    res = client.put(f"/professores/{prof_id}", json={"materia": "Física"})
    assert res.status_code == 200
    assert res.get_json()["materia"] == "Física"

    res = client.delete(f"/professores/{prof_id}")
    assert res.status_code == 200


# ---------- TURMAS ----------
def test_crud_turma(client):
    prof = Professor(nome="Carlos", idade=35, materia="História")
    db.session.add(prof)
    db.session.commit()

    res = client.post("/turmas/", json={
        "descricao": "Turma A - História",
        "professor_id": prof.id,
        "ativo": True
    })
    assert res.status_code == 201
    turma_id = res.get_json()["id"]

    res = client.get(f"/turmas/{turma_id}")
    assert res.status_code == 200

    res = client.put(f"/turmas/{turma_id}", json={"ativo": False})
    assert res.status_code == 200
    assert res.get_json()["ativo"] is False

    res = client.delete(f"/turmas/{turma_id}")
    assert res.status_code == 200


# ---------- ALUNOS ----------
def test_crud_aluno(client):
    prof = Professor(nome="João", idade=45, materia="Geografia")
    db.session.add(prof)
    db.session.commit()

    turma = Turma(descricao="Turma B", professor_id=prof.id, ativo=True)
    db.session.add(turma)
    db.session.commit()

    res = client.post("/alunos/", json={
        "nome": "Ana Clara",
        "idade": 18,
        "turma_id": turma.id,
        "data_nascimento": "2005-03-12",
        "nota_primeiro_semestre": 8.0,
        "nota_segundo_semestre": 9.0,
        "media_final": 8.5
    })
    assert res.status_code == 201
    aluno_id = res.get_json()["id"]

    res = client.get(f"/alunos/{aluno_id}")
    assert res.status_code == 200

    res = client.put(f"/alunos/{aluno_id}", json={"idade": 19})
    assert res.status_code == 200
    assert res.get_json()["idade"] == 19

    res = client.delete(f"/alunos/{aluno_id}")
    assert res.status_code == 200