class StackEmptyException(Exception):
    """Exceção lançada ao tentar desempilhar ou consultar uma pilha vazia."""
    pass


class StackFullException(Exception):
    """Exceção lançada ao tentar empilhar além da capacidade limite."""
    pass


class CustomStack:
    """Estrutura de dados de Pilha (LIFO) com capacidade finita."""

    def __init__(self, limit: int):
        self._limit = limit
        self._elements = []

    def push(self, element) -> None:
        if len(self._elements) >= self._limit:
            raise StackFullException("A pilha atingiu sua capacidade máxima.")
        self._elements.append(element)

    def pop(self):
        if self.is_empty():
            raise StackEmptyException("A pilha está vazia. Não é possível remover elementos.")
        return self._elements.pop()

    def top(self):
        if self.is_empty():
            raise StackEmptyException("A pilha está vazia. Não é possível consultar o topo.")
        return self._elements[-1]

    def is_empty(self) -> bool:
        return len(self._elements) == 0

    def size(self) -> int:
        return len(self._elements)
