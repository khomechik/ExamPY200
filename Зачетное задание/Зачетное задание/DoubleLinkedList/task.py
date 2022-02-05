from typing import Any, Iterable, Optional, Iterator
from collections.abc import MutableSequence

from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):
    NodeName = Node

    def __init__(self, data: Iterable = None):
        self.len = 0
        self.head: Optional[Node] = None
        self.tail = self.head

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = self.NodeName(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """ Функция, которая связывает между собой два узла."""
        left_node.next = right_node

    def __len__(self):
        return self.len

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int):
        """ Метод удаляет значение узла по указанному индексу. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        if index == 0:
            self.head = self.head.next
        elif index == self.len - 1:
            tail = self.step_by_step_on_nodes(index - 1)
            tail.next = None
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            del_node = prev_node.next
            next_node = del_node.next

            self.linked_nodes(prev_node, next_node)

        self.len -= 1

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def insert(self, index, value):
        """ Метод добавляет новый узел по указанному индексу. """
        if not isinstance(index, int):
            raise TypeError
        if index < 0:
            raise IndexError
        if index >= self.len:
            self.append(value)
        elif 0 < index < self.len:
            insert_node = self.NodeName(value)
            current_node = self.step_by_step_on_nodes(index - 1)
            self.linked_nodes(insert_node, current_node.next)
            self.linked_nodes(current_node, insert_node)
            self.len += 1

    def nodes_iterator(self) -> Iterator[Node]:
        """ Функция-генератор для прохода по всем узлам. """
        current_node = self.head
        for _ in range(self.len):
            yield current_node
            current_node = current_node.next

    def __iter__(self) -> Iterator[Any]:
        """ Функция, позволяющая экземплярам класса работать с циклом for. """
        for node in self.nodes_iterator():
            yield node.value

    def __contains__(self, item) -> bool:
        """ Функция показывает, есть ли в последовательности узел с указанным значением. """
        for node in self.nodes_iterator():
            if node.value == item:
                return True
        return False


class DoubleLinkedList(LinkedList):
    NodeName = DoubleLinkedNode

    def __init__(self, data: Iterable = None):
        super().__init__(data=data)

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """ Функция, которая связывает между собой два узла."""
        left_node.next = right_node
        right_node.prev = left_node


if __name__ == "__main__":
    ...
