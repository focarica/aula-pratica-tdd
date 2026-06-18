from aluno.aluno import Aluno


class Turma:
    def __init__(self):
        pass
    
    def contar_aprovados(self, alunos: list[Aluno]) -> int:
        return len([aluno for aluno in alunos if aluno.situacao() == "Aprovado"])