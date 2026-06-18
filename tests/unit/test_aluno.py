import pytest
from unittest.mock import MagicMock
from aluno.aluno import Aluno
from aluno.turma import Turma


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
def test_todos_alunos_aprovados():
    turma = Turma()
    alunos = [
        Aluno("João", [8, 7, 9, 8]), 
        Aluno("Maria", [10, 9, 10, 9])
    ]
    
    assert turma.contar_aprovados(alunos) == 2
    
def test_todos_alunos_reprovados():
    turma = Turma()

    alunos = [
        Aluno("Pedro", [4, 5, 3, 4]), 
        Aluno("Ana", [5, 5, 5, 5])
    ]
    
    assert turma.contar_aprovados(alunos) == 0

def test_lista_alunos_mista():
    turma = Turma()

    alunos = [
        Aluno("João", [8, 7, 9, 8]),   
        Aluno("Pedro", [4, 5, 3, 4]), 
        Aluno("Maria", [10, 9, 10, 9]) 
    ]
    
    assert turma.contar_aprovados(alunos) == 2

def test_lista_alunos_vazia():
    turma = Turma()
    alunos = []
    
    assert turma.contar_aprovados(alunos) == 0

# Requisito 2 — situacao_final(total_aulas) -> str
# Escreva os testes ANTES de implementar o método


# Requisito 3 — enviar_boletim(email_service)
# Use MagicMock para simular o serviço de e-mail
# Escreva os testes ANTES de implementar o método
