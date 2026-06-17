import pytest
from unittest.mock import MagicMock
from aluno.aluno import Aluno


# =============================================================
# PARTE 1 — Encontre os bugs
# Escreva um teste para cada bug descrito no guia da atividade.
# =============================================================
def test_menor_nota_aluno():
    aluno: Aluno = Aluno(
        nome="Artur", 
        notas=[10, 9, 8.8], 
        faltas=12)
    
    assert aluno.menor_nota() == 8.8

def test_nota_media_aluno():
    aluno: Aluno = Aluno(
        nome="Artur", 
        notas=[10, 4.4, 3.6], 
        faltas=12)
    
    assert aluno.calcular_media() == 6.0
    
def test_nota_aluno_exatamente_media():
    aluno: Aluno = Aluno(
        nome="Artur", 
        notas=[6, 6, 6], 
        faltas=12)
    
    assert aluno.situacao() == "Aprovado"
    
def test_media_aluno_arrendodada():
    aluno: Aluno = Aluno(
        nome="Artur", 
        notas=[10, 9.7, 8.9], 
        faltas=12)
    
    assert aluno.calcular_media_arredondada() == 10
#

# =============================================================
# PARTE 2 — Implemente com TDD
# Siga o ciclo: 🔴 escreva o teste → 🟢 implemente → 🟡 refatore
# =============================================================

# Requisito 1 — contar_aprovados(lista_de_alunos) -> int
# Escreva os testes ANTES de implementar a função


# Requisito 2 — situacao_final(total_aulas) -> str
# Escreva os testes ANTES de implementar o método


# Requisito 3 — enviar_boletim(email_service)
# Use MagicMock para simular o serviço de e-mail
# Escreva os testes ANTES de implementar o método
