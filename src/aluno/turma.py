from aluno.aluno import Aluno


class Turma:
    def __init__(self):
        pass
    
    def qtd_aluno_aprovados(self, alunos: list[Aluno]) -> int:
        count = 0
        
        for i in range(len(alunos)):
            if(alunos[i].situacao() == "Aprovado"):
                count += 1
        
        return count