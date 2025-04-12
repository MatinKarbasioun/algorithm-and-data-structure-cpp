from math import trunc
from typing import Any, Iterator

from .node import Node
from ..exception.exceptions import ListEmptyException, KeyDoesNotExist

"""
Lined list real uses:
1- implement other data structure
** queue
** stacks
** graphs

2- Access information by navigating backward and forward
** web browser
** music playlist

"""


class DoublyLinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.__size = 0

    def push_front(self, key: Any):
        new_node = Node(key)
        new_node.next_pointer = self.head
        if self.head:
            self.head.previous_pointer = new_node
        else:
            self.tail = new_node  # list was empty
        self.head = new_node
        self.__size += 1

    def push_back(self, key: Any):
        new_node = Node(key)
        new_node.previous_pointer = self.tail
        if self.tail:
            self.tail.next_pointer = new_node
        else:
            self.head = new_node  # list was empty
        self.tail = new_node
        self.__size += 1

    def top_front(self) -> Any:
        return self.head.key if self.head else None

    def top_back(self) -> Any:
        return self.tail.key if self.tail else None

    def pop_front(self):
        if self.__not_empty():
            key = self.head.key
            self.head = self.head.next_pointer
            if self.head:
                self.head.previous_pointer = None

            else:
                self.tail = None  # list is now empty
            self.__size -= 1
            return key

    def pop_back(self):
        if self.__not_empty():
            key = self.tail.key
            self.tail = self.tail.previous_pointer
            if self.tail:
                self.tail.next_pointer = None
            else:
                self.head = None  # list is now empty
            self.__size -= 1
            return key

    @classmethod
    def add_before(cls, node: Node, key: Any):
        new_node = Node(key)
        new_node.previous_pointer = node.previous_pointer
        new_node.next_pointer = node
        if node.previous_pointer:
            node.previous_pointer.next_pointer = new_node
        node.previous_pointer = new_node

    @classmethod
    def add_after(cls, node: Node, key: Any):
        new_node = Node(key)
        new_node.next_pointer = node.next_pointer
        new_node.previous_pointer = node
        if node.next_pointer:
            node.next_pointer.previous_pointer = new_node
        node.next_pointer = new_node

    def erase(self, key: Any):
        if self.__not_empty():
            current = self.head
            while current and current.key != key:
                current = current.next_pointer

            if not current:
                raise KeyDoesNotExist()

            if current.previous_pointer:
                current.previous_pointer.next_pointer = current.next_pointer

            else:
                self.head = current.next_pointer

            if current.next_pointer:
                current.next_pointer.previous_pointer = current.previous_pointer

            else:
                self.tail = current.previous_pointer

            self.__size -= 1
            return current.key

    def clear(self):
        self.head = None
        self.tail = None
        self.__size = 0

    def empty(self) -> bool:
        return self.head is None

    def find(self, key: Any) -> bool:
        if self.__not_empty():
            current = self.head
            while current:
                if current.key == key:
                    return True
                current = current.next_pointer
            return False

    def search(self, key: Any) -> Node:
        if self.__not_empty():
            current = self.head

            while current:
                if current.key == key:
                    return current

                current = current.next_pointer

            return None

    @property
    def size(self) -> int:
        return self.__size

    def __not_empty(self):
        if self.head:
            return True
        raise ListEmptyException()

    def __iter__(self) -> Iterator[Any]:
        self.current = self.head
        return self

    def __next__(self) -> Any:
        if not self.current:
            raise StopIteration

        key = self.current.key
        self.current = self.current.next_pointer
        return key