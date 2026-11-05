# Exercício Prático - Mock Object (CustomStack & NumberAscOrder)

Projeto desenvolvido com base na estrutura oficial (`custom-stack`), com foco em TDD (Test-Driven Development), testes automatizados com `pytest`, `pytest-cov`, `pytest-mock` e isolamento de dependências através de Mock Objects.

---

## 📁 Estrutura do Projeto

```text
custom-stack/
├── .gitignore
├── pyproject.toml
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── custom_stack_class.py     # Código original da CustomStack (inalterado)
│   └── number_asc_order.py       # Classe de ordenação usando CustomStack
└── test/
    ├── __init__.py
    ├── custom_stack_test.py      # Testes auditados e expandidos para 100% de cobertura
    └── number_asc_order_test.py  # Testes de unidade com Mocks para NumberAscOrder
```

---

## 🚀 Instalação e Execução

### 1. Criar e Ativar o Ambiente Virtual

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 3. Executar os Testes e Relatório de Cobertura (100%)

```bash
# Execução direta com pytest e cobertura
pytest --cov

# Execução detalhada com term-missing
pytest -v --cov --cov-report=term-missing
```

---

## 🧪 Cobertura dos Cenários de Teste

### 1. `test/custom_stack_test.py`
- Preservado o teste original do professor (`test_push_one_elementinstack`).
- Inserção de múltiplos elementos e manutenção da ordem LIFO.
- Tentativa de `push` atingindo o limite configurado (lança `StackFullException`).
- Remoção (`pop`) retornando o elemento correto do topo e decrementando tamanho.
- Tentativa de `pop` em pilha vazia (lança `StackEmptyException`).
- Tentativa de `pop` após esvaziar a pilha (lança `StackEmptyException`).
- Consulta de `top` sem remoção do elemento.
- Consulta de `top` em pilha vazia (lança `StackEmptyException`).
- Instanciação e herança das exceções customizadas.

### 2. `test/number_asc_order_test.py`
- **Cenário 1 (Mega Sena):** Mock de `CustomStack` simulando 6 números sorteados da Mega Sena não ordenados, `is_empty.side_effect = [False, False, False, False, False, False, True]`, `pop.side_effect` com os 6 números. Valida retorno com 6 elementos, estritamente ordenados e `mock_stack.pop.call_count == 6`.
- **Cenário 2 (Pilha Vazia):** Mock configurado com `is_empty.return_value = True`. Valida retorno `[]`, `mock_stack.is_empty.assert_called_once()` e `mock_stack.pop.assert_not_called()`.
- **Cenários Extras:** Validação de parâmetro nulo (`None`) levantando `TypeError` e tratamento resiliente de `StackEmptyException`.

---

## 📊 Relatório de Cobertura

```text
Name                        Stmts   Miss Branch BrPart  Cover   Missing
-----------------------------------------------------------------------
src\__init__.py                 0      0      0      0   100%
src\custom_stack_class.py      24      0      6      0   100%
src\number_asc_order.py        12      0      4      0   100%
-----------------------------------------------------------------------
TOTAL                          36      0     10      0   100%
```
**100% de cobertura de código e branches atingidos!**
