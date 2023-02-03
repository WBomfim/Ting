from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    _queue: list

    def __init__(self):
        self._queue = []

    def __len__(self):
        return len(self._queue)

    def enqueue(self, value):
        self._queue.append(value)

    def dequeue(self):
        if len(self._queue) == 0:
            raise IndexError('Queue is empty')

        return self._queue.pop(0)

    def search(self, index):
        if not 0 <= index < len(self._queue):
            raise IndexError('Index out of range')

        return self._queue[index]
