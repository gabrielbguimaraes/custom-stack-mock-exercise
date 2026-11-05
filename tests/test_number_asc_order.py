import random
import pytest
from unittest.mock import MagicMock
from src.custom_stack import CustomStack, StackEmptyException
from src.number_asc_order import NumberAscOrder


class TestNumberAscOrder:
    """Testes unitários para NumberAscOrder utilizando Mock Objects para isolar CustomStack."""

    def test_scenario_1_stack_with_six_random_mega_sena_numbers(self):
        """Cenário 1: Pilha com 6 números sorteados da Mega Sena (entre 1 e 60, não ordenados).

        Valida que o resultado possui 6 elementos em ordem estritamente ascendente e
        que pop() foi chamado exatamente 6 vezes.
        """
        # Sorteio de 6 números distintos entre 1 e 60
        mega_sena_numbers = [42, 17, 59, 10, 43, 57]
        # Garante que a entrada não está previamente ordenada
        assert mega_sena_numbers != sorted(mega_sena_numbers)

        mock_stack = MagicMock(spec=CustomStack)
        mock_stack.is_empty.side_effect = [False, False, False, False, False, False, True]
        mock_stack.pop.side_effect = list(mega_sena_numbers)

        order_service = NumberAscOrder()
        result = order_service.sort(mock_stack)

        assert len(result) == 6
        assert result == sorted(mega_sena_numbers)
        assert result == [10, 17, 42, 43, 57, 59]
        assert mock_stack.pop.call_count == 6

    def test_scenario_1_with_dynamic_random_sample(self):
        """Variação do Cenário 1 garantindo conformidade com valores dinamicamente aleatórios."""
        random_numbers = random.sample(range(1, 61), 6)
        while random_numbers == sorted(random_numbers):
            random_numbers = random.sample(range(1, 61), 6)

        mock_stack = MagicMock(spec=CustomStack)
        mock_stack.is_empty.side_effect = [False, False, False, False, False, False, True]
        mock_stack.pop.side_effect = list(random_numbers)

        order_service = NumberAscOrder()
        result = order_service.sort(mock_stack)

        assert len(result) == 6
        assert result == sorted(random_numbers)
        assert mock_stack.pop.call_count == 6

    def test_scenario_2_empty_stack_returns_empty_list(self):
        """Cenário 2: Pilha vazia deve retornar lista vazia sem efetuar pop().

        Valida que o retorno é [], is_empty foi chamado uma vez e pop() nunca foi chamado.
        """
        mock_stack = MagicMock(spec=CustomStack)
        mock_stack.is_empty.return_value = True

        order_service = NumberAscOrder()
        result = order_service.sort(mock_stack)

        assert result == []
        mock_stack.is_empty.assert_called_once()
        mock_stack.pop.assert_not_called()

    def test_scenario_extra_invalid_parameter_none_raises_type_error(self):
        """Cenário Extra: Valida que sort(None) levanta TypeError com mensagem clara."""
        order_service = NumberAscOrder()

        with pytest.raises(TypeError) as exc_info:
            order_service.sort(None)

        assert "não pode ser None" in str(exc_info.value)

    def test_scenario_extra_pop_raises_stack_empty_exception(self):
        """Cenário Extra: Valida tratamento robusto caso pop() levante StackEmptyException durante o laço."""
        mock_stack = MagicMock(spec=CustomStack)
        mock_stack.is_empty.side_effect = [False, False, True]
        mock_stack.pop.side_effect = [25, StackEmptyException("Pilha vazia inesperadamente")]

        order_service = NumberAscOrder()
        result = order_service.sort(mock_stack)

        assert result == [25]
        assert mock_stack.pop.call_count == 2
