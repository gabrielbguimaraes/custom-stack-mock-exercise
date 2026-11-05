import pytest
from src.custom_stack import CustomStack, StackEmptyException, StackFullException


class TestCustomStack:
    """Testes unitários rigorosos e de alta efetividade para a CustomStack."""

    def test_should_initialize_empty_stack_with_zero_size(self):
        """Verifica se a pilha é inicializada vazia e com tamanho 0."""
        stack = CustomStack(limit=5)
        assert stack.is_empty() is True
        assert stack.size() == 0

    def test_should_push_element_within_limit_and_update_state(self):
        """Verifica a inserção dentro do limite, validando size, top e is_empty."""
        stack = CustomStack(limit=3)
        stack.push(10)

        assert stack.is_empty() is False
        assert stack.size() == 1
        assert stack.top() == 10

    def test_should_push_multiple_elements_maintaining_order(self):
        """Verifica múltiplos empilhamentos respeitando o comportamento LIFO."""
        stack = CustomStack(limit=3)
        stack.push(10)
        stack.push(20)
        stack.push(30)

        assert stack.size() == 3
        assert stack.top() == 30
        assert stack.is_empty() is False

    def test_should_raise_stack_full_exception_when_reaching_limit(self):
        """Verifica se lança StackFullException ao atingir e tentar exceder a capacidade máxima."""
        stack = CustomStack(limit=2)
        stack.push(100)
        stack.push(200)

        assert stack.size() == 2
        with pytest.raises(StackFullException):
            stack.push(300)

        # O estado da pilha deve permanecer inalterado
        assert stack.size() == 2
        assert stack.top() == 200

    def test_should_pop_element_returning_correct_value_and_decrementing_size(self):
        """Verifica a remoção (pop), validando retorno, redução de tamanho e topo anterior."""
        stack = CustomStack(limit=3)
        stack.push(10)
        stack.push(20)

        popped_value = stack.pop()

        assert popped_value == 20
        assert stack.size() == 1
        assert stack.top() == 10
        assert stack.is_empty() is False

        # Desempilha o elemento restante
        second_popped = stack.pop()
        assert second_popped == 10
        assert stack.size() == 0
        assert stack.is_empty() is True

    def test_should_raise_stack_empty_exception_when_popping_from_empty_stack(self):
        """Verifica se lança StackEmptyException ao tentar desempilhar de pilha vazia."""
        stack = CustomStack(limit=3)
        assert stack.is_empty() is True

        with pytest.raises(StackEmptyException):
            stack.pop()

        assert stack.size() == 0

    def test_should_raise_stack_empty_exception_when_popping_after_emptying(self):
        """Verifica se lança StackEmptyException ao tentar desempilhar de pilha que foi esvaziada."""
        stack = CustomStack(limit=2)
        stack.push(42)
        stack.pop()
        assert stack.is_empty() is True

        with pytest.raises(StackEmptyException):
            stack.pop()

    def test_should_consult_top_without_removing_element(self):
        """Verifica se a consulta a top() retorna o elemento sem removê-lo."""
        stack = CustomStack(limit=3)
        stack.push(99)

        assert stack.top() == 99
        assert stack.top() == 99  # Chamada subsequente não remove
        assert stack.size() == 1
        assert stack.is_empty() is False

    def test_should_raise_stack_empty_exception_when_consulting_top_on_empty_stack(self):
        """Verifica se lança StackEmptyException ao consultar top() em pilha vazia."""
        stack = CustomStack(limit=3)
        assert stack.is_empty() is True

        with pytest.raises(StackEmptyException):
            stack.top()

    def test_exceptions_inheritance_and_instantiation(self):
        """Garante cobertura e herança correta das classes de exceção."""
        empty_exc = StackEmptyException("vazia")
        full_exc = StackFullException("cheia")

        assert isinstance(empty_exc, Exception)
        assert isinstance(full_exc, Exception)
        assert str(empty_exc) == "vazia"
        assert str(full_exc) == "cheia"
