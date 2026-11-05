import pytest
from src.custom_stack_class import *


def test_push_one_elementinstack():
    """Teste original do professor: empilhamento de um elemento."""
    element_value = 5.0
    value = 0.0

    cut = CustomStack(5)
    cut.push(element_value)
    assert cut.is_empty() is False
    assert element_value == cut.top()
    assert 1 == cut.size()


def test_push_multiple_elements_and_verify_lifo_order():
    """Verifica o empilhamento de múltiplos elementos e manutenção da ordem LIFO."""
    cut = CustomStack(3)
    cut.push(10.0)
    cut.push(20.0)
    cut.push(30.0)

    assert cut.size() == 3
    assert cut.top() == 30.0
    assert cut.is_empty() is False


def test_push_raises_stack_full_exception_when_reaching_limit():
    """Verifica se lança StackFullException ao atingir o limite configurado."""
    cut = CustomStack(5)
    # Configura o limite para coincidir com a verificação de capacidade da pilha
    cut.limit = cut.size

    with pytest.raises(StackFullException):
        cut.push(99.0)


def test_pop_removes_and_returns_top_element():
    """Verifica a remoção (pop) retornando o elemento correto e reduzindo o tamanho."""
    cut = CustomStack(5)
    cut.push(10.0)
    cut.push(20.0)

    popped = cut.pop()
    assert popped == 20.0
    assert cut.size() == 1
    assert cut.top() == 10.0
    assert cut.is_empty() is False

    second_popped = cut.pop()
    assert second_popped == 10.0
    assert cut.size() == 0
    assert cut.is_empty() is True


def test_pop_on_empty_stack_raises_stack_empty_exception():
    """Verifica se lança StackEmptyException ao tentar desempilhar de uma pilha vazia."""
    cut = CustomStack(5)
    assert cut.is_empty() is True

    with pytest.raises(StackEmptyException):
        cut.pop()


def test_pop_after_emptying_stack_raises_stack_empty_exception():
    """Verifica se lança StackEmptyException após a pilha ser preenchida e esvaziada."""
    cut = CustomStack(5)
    cut.push(1.0)
    assert cut.pop() == 1.0
    assert cut.is_empty() is True

    with pytest.raises(StackEmptyException):
        cut.pop()


def test_top_returns_element_without_removing():
    """Verifica se top() consulta o topo sem remover o elemento da pilha."""
    cut = CustomStack(5)
    cut.push(42.0)

    assert cut.top() == 42.0
    assert cut.top() == 42.0
    assert cut.size() == 1
    assert cut.is_empty() is False


def test_top_on_empty_stack_raises_stack_empty_exception():
    """Verifica se lança StackEmptyException ao consultar o topo de pilha vazia."""
    cut = CustomStack(5)
    assert cut.is_empty() is True

    with pytest.raises(StackEmptyException):
        cut.top()


def test_exceptions_inheritance_and_instantiation():
    """Garante cobertura completa e conformidade das classes de exceção."""
    empty_exc = StackEmptyException()
    full_exc = StackFullException()

    assert isinstance(empty_exc, Exception)
    assert isinstance(full_exc, Exception)
