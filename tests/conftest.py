import pytest
from calculadora.calculadora import Aluno


@pytest.fixture
def aluno_aprovado():
    return Aluno(nome="Maria", notas=[8, 9, 7, 8], faltas=2)


@pytest.fixture
def aluno_reprovado():
    return Aluno(nome="João", notas=[4, 3, 5, 4], faltas=2)
