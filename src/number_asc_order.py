from src.custom_stack_class import CustomStack, StackEmptyException


class NumberAscOrder:
    """Serviço para desempilhar e ordenar elementos numéricos de forma ascendente."""

    def sort(self, stack: CustomStack) -> list:
        """Desempilha os elementos de uma pilha e os retorna em ordem crescente.

        Args:
            stack (CustomStack): Pilha contendo os elementos a serem extraídos e ordenados.

        Returns:
            list: Lista contendo os números ordenados de forma ascendente.

        Raises:
            TypeError: Se o parâmetro stack for None.
        """
        if stack is None:
            raise TypeError("O parâmetro stack não pode ser None.")

        numbers = []
        while not stack.is_empty():
            try:
                numbers.append(stack.pop())
            except StackEmptyException:
                break

        return sorted(numbers)
