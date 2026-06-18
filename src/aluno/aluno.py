class Aluno:
    def __init__(self, nome: str, notas: list, faltas: int = 0):
        self.nome = nome
        self.notas = notas
        self.faltas = faltas

    def calcular_media(self) -> float:
        return sum(self.notas) / len(self.notas)

    def situacao(self) -> str:
        if self.calcular_media() >= 6.0:
            return "Aprovado"
        return "Reprovado"

    def situacao_final(self, total_aulas: int) -> str:
        if((self.faltas / total_aulas) > 0.25):
            return "Reprovado por Falta"
        elif(sum(self.notas) / len(self.notas) >= 6.0):
            return "Aprovado"
        else:
            return "Reprovado por Nota"

    def maior_nota(self) -> float:
        return max(self.notas)

    def menor_nota(self) -> float:
        return min(self.notas)

    def calcular_media_arredondada(self) -> float:
        return round(sum(self.notas) / len(self.notas))
