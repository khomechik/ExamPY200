from typing import Any, Optional


class Node:

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        self.value = value
        self.next = next_

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"Node({self.value}, {self.next})"

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError("Value of inappropriate type")

    @property
    def prop_next(self):
        return self._next

    @prop_next.setter
    def prop_next(self, next_: Optional["Node"]):
        if self.is_valid(next_):
            self._next = next_


class DoubleLinkedNode(Node):
    def __init__(self, value=None, next_=None, prev=None):
        super().__init__(value=value, next_=next_)
        self._prev = prev

    def __repr__(self) -> str:
        prev = None if self.prev is None else f"DoubleLinkedNode({self.prev})"
        next_ = None if self.next is None else f"DoubleLinkedNode({self.next})"
        return f"DoubleLinkedNode({self.value}), {next_}, {prev}"

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), DoubleLinkedNode)):
            raise TypeError("Value of inappropriate type")

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev):
        if self.is_valid(prev):
            self._prev = prev


if __name__ == "__main__":
    ...
