from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.items = []
        self.processed_files = []

    def __len__(self):
        return len(self.items)

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if len(self) == 0:
            raise IndexError("A fila está vazia")
        return self.items.pop(0)

    def is_duplicate(self, path_file):
        return path_file in self.processed_files

    def search(self, index):
        if not (0 <= index < len(self)):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.items[index]
