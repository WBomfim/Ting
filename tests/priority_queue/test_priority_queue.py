import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()
    priority_queue.enqueue({"qtd_linhas": 9})
    priority_queue.enqueue({"qtd_linhas": 4})
    priority_queue.enqueue({"qtd_linhas": 2})
    priority_queue.enqueue({"qtd_linhas": 5})
    priority_queue.enqueue({"qtd_linhas": 7})
    priority_queue.enqueue({"qtd_linhas": 11})
    priority_queue.enqueue({"qtd_linhas": 3})

    """Verifica o tamanho total da fila"""
    assert len(priority_queue) == 7

    """Verifica o tamanho da fila de prioridade alta"""
    assert len(priority_queue.high_priority) == 3

    """Verifica o tamanho da fila de prioridade baixa"""
    assert len(priority_queue.regular_priority) == 4

    """Verifica a correta remoção de um elemento da fila"""
    assert priority_queue.dequeue() == {"qtd_linhas": 4}
    assert len(priority_queue) == 6

    assert priority_queue.dequeue() == {"qtd_linhas": 2}
    assert len(priority_queue) == 5

    """Verifica se a pesquisa de um elemento da fila é feita corretamente"""
    assert priority_queue.search(0) == {"qtd_linhas": 3}
    assert priority_queue.search(1) == {"qtd_linhas": 9}
    assert priority_queue.search(2) == {"qtd_linhas": 5}

    """Verifica se a pesquisa lança uma exceção quando o índice é inválido"""
    with pytest.raises(IndexError):
        priority_queue.search(-1)

    with pytest.raises(IndexError):
        priority_queue.search(10)
