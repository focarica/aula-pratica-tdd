# Atividade Prática — Calculadora de Notas

> **Objetivo:** praticar escrita de testes para encontrar bugs e implementar novos requisitos seguindo o ciclo TDD.

---

## Configuração do ambiente

```bash
# 1. Entre na pasta do projeto
cd calculadora_notas

# 2. Crie o ambiente virtual
python -m venv .venv

# 3. Ative o ambiente
source .venv/bin/activate      # Linux/Mac
.venv\Scripts\activate         # Windows

# 4. Instale as dependências
pip install -r requirements.txt

# 5. Confirme que o pytest está funcionando
pytest
```

> Os testes passam porque estão vazios (`pass`). Sua missão é preenchê-los.

---

## Estrutura do projeto

```
calculadora_notas/
├── src/
│   └── calculadora/
│       ├── __init__.py
│       └── calculadora.py       ← código com bugs (não altere ainda)
├── tests/
│   ├── conftest.py              ← fixtures prontas para usar
│   └── unit/
│       └── test_calculadora.py  ← seus testes ficam aqui
├── pytest.ini
└── requirements.txt
```

---

## O código

A classe `Aluno` já está implementada em `src/calculadora/calculadora.py`:

```python
class Aluno:
    def __init__(self, nome: str, notas: list, faltas: int = 0):
        self.nome = nome
        self.notas = notas
        self.faltas = faltas

    def calcular_media(self) -> float:
        ...

    def situacao(self) -> str:
        ...

    def maior_nota(self) -> float:
        ...

    def menor_nota(self) -> float:
        ...

    def calcular_media_arredondada(self) -> float:
        ...
```

O código **roda sem erros** — mas possui **4 bugs escondidos**.

---

## Fixtures disponíveis

No `conftest.py` já existem dois objetos prontos para usar nos testes:

```python
# aluno com notas boas
def test_exemplo(aluno_aprovado):
    print(aluno_aprovado.nome)   # "Maria"
    print(aluno_aprovado.notas)  # [8, 9, 7, 8]

# aluno com notas baixas
def test_exemplo(aluno_reprovado):
    print(aluno_reprovado.nome)   # "João"
    print(aluno_reprovado.notas)  # [4, 3, 5, 4]
```

---

## Como rodar os testes

```bash
# rodar todos
pytest

# rodar e ver detalhes
pytest -v

# rodar um teste específico
pytest tests/unit/test_calculadora.py::test_bug_1_calcular_media

# parar no primeiro erro
pytest -x

# ver cobertura ao final
pytest --cov=src/calculadora --cov-report=term-missing
```

---

---

# PARTE 1 — Encontre os bugs

> **Regra:** abra apenas o arquivo `tests/unit/test_calculadora.py`.
> Não altere o `calculadora.py` ainda.

---

## Como funciona

Você vai escrever um teste, rodar o pytest, e observar se ele **falha**.

Se o teste falhar → você encontrou o bug.
Se o teste passar → o teste não está cobrindo o caso certo, tente outro valor.


## Após encontrar todos os bugs

Corrija o `calculadora.py` e rode os testes novamente. Todos devem passar.

```bash
pytest tests/unit/test_calculadora.py -v
```

---

# PARTE 2 — Implemente com TDD

> **Regra do TDD:** escreva o teste **antes** do código de produção.
> O ciclo é sempre: 🔴 RED → 🟢 GREEN → 🟡 REFACTOR

---

## O ciclo na prática

```
🔴 RED     → escreva o teste (ele deve FALHAR)
🟢 GREEN   → escreva o mínimo de código para passar
🟡 REFACTOR → melhore o código sem quebrar os testes
```

> **Nunca pule o RED.** Se o teste passou sem você escrever o código — o teste está errado.

---

## Requisito 1 — `contar_aprovados()`

**O que deve fazer:**
Receber uma lista de objetos `Aluno` e retornar quantos foram aprovados.

**Assinatura esperada:**
```python
def contar_aprovados(alunos: list) -> int:
    ...
```

**Casos que você deve testar:**

| Cenário | Entrada | Esperado |
|---|---|---|
| Todos aprovados | 3 alunos com média >= 6 | 3 |
| Todos reprovados | 3 alunos com média < 6 | 0 |
| Misto | 2 aprovados, 1 reprovado | 2 |
| Lista vazia | `[]` | 0 |

**Passo a passo:**

1. Escreva o primeiro teste (cenário mais simples)
2. Rode o pytest → deve **falhar** (função não existe)
3. Implemente o mínimo para passar
4. Escreva o próximo teste
5. Repita até cobrir todos os cenários

> **Dica:** a função `contar_aprovados` pode ficar em `calculadora.py`, fora da classe.

---

## Requisito 2 — `situacao_final()`

**O que deve fazer:**
Novo método da classe `Aluno` que considera também as **faltas** na situação final.

**Assinatura esperada:**
```python
def situacao_final(self, total_aulas: int) -> str:
    ...
```

**Regras:**

| Condição | Retorno |
|---|---|
| Faltas > 25% do total de aulas | `"Reprovado por Falta"` |
| Faltas dentro do limite e média >= 6.0 | `"Aprovado"` |
| Faltas dentro do limite e média < 6.0 | `"Reprovado por Nota"` |

**Casos que você deve testar:**

```python
# aluno com muitas faltas
aluno = Aluno(nome="Ana", notas=[8, 9, 8, 9], faltas=10)
aluno.situacao_final(total_aulas=30)  # → "Reprovado por Falta"

# aluno aprovado
aluno = Aluno(nome="Ana", notas=[8, 9, 8, 9], faltas=2)
aluno.situacao_final(total_aulas=30)  # → "Aprovado"

# aluno reprovado por nota
aluno = Aluno(nome="Ana", notas=[4, 3, 5, 4], faltas=2)
aluno.situacao_final(total_aulas=30)  # → "Reprovado por Nota"

# caso de borda — exatamente 25% de faltas
aluno = Aluno(nome="Ana", notas=[8, 9, 8, 9], faltas=8)
aluno.situacao_final(total_aulas=32)  # → o que deve acontecer aqui?
```

> **Dica:** pense no caso de borda antes de implementar. Exatamente 25% é reprovado ou não?

---

## Requisito 3 — `enviar_boletim()` com MagicMock

**O que deve fazer:**
Método da classe `Aluno` que chama um serviço externo de e-mail.

**Assinatura esperada:**
```python
def enviar_boletim(self, email_service) -> None:
    ...
```

**Regras:**
- Se o aluno estiver **reprovado** → chama `email_service.enviar(nome, media)`
- Se o aluno estiver **aprovado** → **não** chama o `email_service`

---

### Por que usar MagicMock?

O `email_service` na vida real dispararia um e-mail de verdade. Nos testes, não queremos isso. O `MagicMock` é um objeto falso que finge ser o serviço e permite verificar se ele foi chamado.

```python
from unittest.mock import MagicMock

# criar o serviço falso
mock_email = MagicMock()

# programar o comportamento (se necessário)
mock_email.enviar.return_value = True

# verificar se foi chamado
mock_email.enviar.assert_called_once()

# verificar se foi chamado com argumentos específicos
mock_email.enviar.assert_called_once_with("João", 4.0)

# verificar se NÃO foi chamado
mock_email.enviar.assert_not_called()
```

---

### Testes que você deve escrever

**Teste 1 — aluno reprovado deve receber e-mail:**
```python
def test_envia_boletim_aluno_reprovado():
    aluno = Aluno(nome="João", notas=[4, 4, 4, 4])
    mock_email = MagicMock()

    aluno.enviar_boletim(mock_email)

    # verifique que enviar() foi chamado com os dados corretos
```

**Teste 2 — aluno aprovado não deve receber e-mail:**
```python
def test_nao_envia_boletim_aluno_aprovado():
    aluno = Aluno(nome="Maria", notas=[8, 8, 8, 8])
    mock_email = MagicMock()

    aluno.enviar_boletim(mock_email)

    # verifique que enviar() NÃO foi chamado
```

---

## Resultado esperado ao final

```bash
pytest --cov=src/calculadora --cov-report=term-missing
```

```
tests/unit/test_calculadora.py
  test_contar_todos_aprovados            PASSED ✓
  test_contar_todos_reprovados           PASSED ✓
  test_contar_aprovados_misto            PASSED ✓
  test_contar_aprovados_lista_vazia      PASSED ✓
  test_situacao_final_reprovado_falta    PASSED ✓
  test_situacao_final_aprovado           PASSED ✓
  test_situacao_final_reprovado_nota     PASSED ✓
  test_situacao_final_borda_faltas       PASSED ✓
  test_envia_boletim_aluno_reprovado     PASSED ✓
  test_nao_envia_boletim_aluno_aprovado  PASSED ✓

---------- coverage -----------
calculadora.py    100%
```

