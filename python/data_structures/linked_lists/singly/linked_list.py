from typing import Any, Iterator

from .node import Node
from ..exception.exceptions import ListEmptyException, NodeDoesNotExist, KeyDoesNotExist

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

class SinglyLinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.current = self.head
        self.__size = 0

    def push_front(self, key: Any):
        self.__size += 1
        new_node = Node(key)
        new_node.next_pointer = self.head
        self.head = new_node

        if not self.tail:
            self.tail = self.head

    def push_back(self, key: Any):
        self.__size += 1
        new_node = Node(key)

        if self.head:
            self.tail.next_pointer = new_node
            self.tail = new_node

        else:
            self.head = new_node
            self.tail = new_node

    def top_front(self) -> Any:
        return self.head.key if self.head else None

    def top_back(self) -> Any:
        return self.tail.key if self.tail else None

    def pop_front(self):
        if self.__not_empty():
            self.__size -= 1
            key = self.head.key
            self.head = self.head.next_pointer

            if not self.head:
                self.tail = None

            return key

    def pop_back(self):
        if self.__not_empty():
            self.__size -= 1

            if self.head == self.tail:
               self.head = self.tail = None

            else:
               current_node = self.head

               while current_node.next_pointer != self.tail:
                  current_node = current_node.next_pointer

               current_node.next_pointer = None

               self.tail = current_node

    def add_before(self, node: Node, key: Any):

        if self.head == node:
            self.push_front(key)
            return

        current_node = self.head

        while current_node.next_pointer and current_node.next_pointer != node:
            current_node = current_node.next_pointer

        if current_node.next_pointer != node:
            raise NodeDoesNotExist()

        new_node = Node(key)
        new_node.next_pointer = node
        current_node.next_pointer = new_node
        self.__size += 1

    @classmethod
    def add_after(cls, node: Node, key: Any):
        new_node = Node(key)
        new_node.next_pointer = node.next_pointer
        node.next_pointer = new_node

    def erase(self, key: Any):
        if self.__not_empty():
            current_node = self.head

            if current_node.key == key:
                self.head = self.head.next_pointer
                self.__size -= 1

                if not self.head:
                    self.tail = None

                return

            while current_node.next_pointer and current_node.next_pointer.key != key:
                current_node.next_pointer = current_node.next_pointer.next_pointer.next_pointer


            if not current_node.next_pointer:
                raise KeyDoesNotExist()

            current_node.next_pointer = current_node.next_pointer.next_pointer
            self.__size -= 1



    def clear(self):
        self.head = self.tail = None
        self.__size = 0

    def empty(self) -> bool:
        return self.head is None

    def find(self, key: Any) -> bool:
        if self.__not_empty():
            return self.head.find(key)

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
