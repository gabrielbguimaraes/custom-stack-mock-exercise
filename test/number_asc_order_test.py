import random
import pytest
from unittest.mock import MagicMock
from src.custom_stack_class import CustomStack, StackEmptyException
from src.number_asc_order import NumberAscOrder


def test_scenario_1_stack_with_six_random_mega_sena_numbers():
    """Cenário 1: Pilha de 6 posições com 6 números sorteados da Mega Sena (1 a 60, não ordenados).

    Configura is_empty.side_effect com 6 False e 1 True, e pop.side_effect com os 6 números.
    Valida 6 elementos no retorno, ordem estritamente crescente e pop.call_count == 6.
    """
    mega_sena_numbers = [42, 17, 59, 10, 43, 57]
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


def test_scenario_1_dynamic_random_sample():
    """Variação do Cenário 1 com números sorteados dinamicamente via random.sample."""
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


def test_scenario_2_empty_stack_returns_empty_list():
    """Cenário 2: Pilha vazia deve retornar lista vazia [].

    Valida que is_empty foi chamado exatamente uma vez e que pop não foi chamado.
    """
    mock_stack = MagicMock(spec=CustomStack)
    mock_stack.is_empty.return_value = True

    order_service = NumberAscOrder()
    result = order_service.sort(mock_stack)

    assert result == []
    mock_stack.is_empty.assert_called_once()
    mock_stack.pop.assert_not_called()


def test_scenario_extra_invalid_parameter_none_raises_type_error():
    """Cenário Extra: Valida que sort(None) levanta TypeError com mensagem explicativa."""
    order_service = NumberAscOrder()

    with pytest.raises(TypeError) as exc_info:
        order_service.sort(None)

    assert "não pode ser None" in str(exc_info.value)


def test_scenario_extra_pop_raises_stack_empty_exception_handled():
    """Cenário Extra: Valida tratamento resiliente caso pop() levante StackEmptyException durante o laço."""
    mock_stack = MagicMock(spec=CustomStack)
    mock_stack.is_empty.side_effect = [False, False]
    mock_stack.pop.side_effect = [25, StackEmptyException("Pilha esvaziada")]

    order_service = NumberAscOrder()
    result = order_service.sort(mock_stack)

    assert result == [25]
    assert mock_stack.pop.call_count == 2
