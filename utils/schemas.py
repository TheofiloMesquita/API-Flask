from flasgger import Schema, fields

class ProfessorSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True, description="Nome do professor")
    idade = fields.Int(required=True, description="Idade do professor")
    materia = fields.Str(required=True, description="Matéria que o professor leciona")
    observacoes = fields.Str(description="Informações adicionais")


class TurmaSchema(Schema):
    id = fields.Int(dump_only=True)
    descricao = fields.Str(required=True, description="Descrição da turma")
    professor_id = fields.Int(required=True, description="ID do professor responsável")
    ativo = fields.Bool(required=True, description="Se a turma está ativa")


class AlunoSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True, description="Nome do aluno")
    idade = fields.Int(required=True, description="Idade do aluno")
    turma_id = fields.Int(required=True, description="ID da turma que o aluno pertence")
    data_nascimento = fields.Date(required=True, description="Data de nascimento (YYYY-MM-DD)")
    nota_primeiro_semestre = fields.Float(required=True, description="Nota do primeiro semestre")
    nota_segundo_semestre = fields.Float(required=True, description="Nota do segundo semestre")
    media_final = fields.Float(description="Média final do aluno")