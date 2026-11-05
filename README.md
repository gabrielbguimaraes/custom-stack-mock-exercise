# Exercício Prático - Mock Object (CustomStack & NumberAscOrder)

Projeto desenvolvido com foco em TDD (Test-Driven Development), testes automatizados com `pytest`, `pytest-cov`, `pytest-mock` e isolamento de dependências com Mock Objects.

## 📋 Sobre o Projeto

O projeto é composto por dois módulos principais:
1. **`CustomStack` (`src/custom_stack.py`)**: Estrutura de dados de pilha (LIFO) de tamanho delimitado, com métodos para inserção (`push`), remoção (`pop`), consulta de topo (`top`), verificação de vazio (`is_empty`) e consulta de tamanho (`size`). Lança exceções customizadas `StackFullException` e `StackEmptyException`.
2. **`NumberAscOrder` (`src/number_asc_order.py`)**: Serviço responsável por desempilhar elementos de uma instância de `CustomStack` e retorná-los ordenados em ordem ascendente (`sort(stack)`). Isola a dependência da pilha em seus testes unitários através de Mock Objects (`unittest.mock.MagicMock`).

---

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos
- Python 3.10+ (ou superior)

### 2. Criar e Ativar o Ambiente Virtual

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Executar os Testes e Relatório de Cobertura (100%)

```bash
# Execução simples com cobertura
pytest --cov

# Execução detalhada com linhas faltantes (term-missing)
pytest -v --cov --cov-report=term-missing
```

---

## 🧪 Estrutura de Testes

- **`tests/test_custom_stack.py`**:
  - Inicialização de pilha vazia e tamanho zero.
  - Empilhamento (`push`) dentro do limite, validando `size()`, `top()` e `is_empty()`.
  - Empilhamento além da capacidade máxima, validando o lançamento de `StackFullException`.
  - Desempilhamento (`pop`) retornando o elemento correto do topo e reduzindo o tamanho.
  - Desempilhamento em pilha vazia, validando o lançamento de `StackEmptyException`.
  - Consulta de topo (`top`) sem remoção do elemento.
  - Consulta de topo em pilha vazia, validando o lançamento de `StackEmptyException`.
  - Instanciação e herança das exceções customizadas.

- **`tests/test_number_asc_order.py`**:
  - **Cenário 1 (Mega Sena):** Mock de pilha com 6 números sorteados não ordenados da Mega Sena, simulando `is_empty.side_effect = [False, False, False, False, False, False, True]`, validando que o retorno possui 6 elementos estritamente em ordem crescente e que `mock.pop.call_count == 6`.
  - **Cenário 2 (Pilha Vazia):** Mock configurado com `is_empty.return_value = True`, validando retorno de lista vazia `[]`, `is_empty.assert_called_once()` e `mock.pop.assert_not_called()`.
  - **Cenários Extras:** Validação de parâmetro nulo (`None`) levantando `TypeError` e tratamento de `StackEmptyException` inesperada durante o esvaziamento.

---

## 📊 Relatório de Cobertura

```
Name                      Stmts   Miss Branch BrPart  Cover   Missing
---------------------------------------------------------------------
src\__init__.py               0      0      0      0   100%
src\custom_stack.py          24      0      6      0   100%
src\number_asc_order.py      12      0      4      0   100%
---------------------------------------------------------------------
TOTAL                        36      0     10      0   100%
```
**100% de cobertura de código e branches atingidos!**
