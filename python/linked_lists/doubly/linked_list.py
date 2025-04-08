from dataclasses import dataclass
from typing import Any

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

@dataclass
class DoublyLinkedList:
    head: Node | None = None
    tail: Node | None = None

    def push_front(self, key: Any):
        new_node = Node(key)
        new_node.next_pointer = self.head
        self.head = new_node

        if not self.tail:
            self.tail = self.head

    def push_back(self, key: Any):
        new_node = Node(key)

        if self.head:
            new_node.previous_pointer = self.tail.previous_pointer
            new_node.next_pointer = self.tail.next_pointer
            self.tail.next_pointer = new_node
            self.tail = new_node

        else:
            self.head = new_node
            self.tail = new_node

    def top_front(self) -> Any:
        if self.__not_empty():
            return self.head.key

    def top_back(self) -> Any:
        if self.__not_empty():
            return self.tail.key

    def pop_front(self):
        if self.__not_empty():
            key = self.head.key
            self.head = self.head.next_pointer

            if not self.head:
                self.tail = None

            return key

        else:
            return None

    def pop_back(self):
        if self.__not_empty():
           if self.head == self.tail:
               key = self.head.key
               self.head = None
               self.tail = None

           else:
               key = self.tail.key
               substitution_node = self.tail.previous_pointer
               substitution_node.next_pointer = None
               self.tail = substitution_node

           return key

        else:
            return None

    @classmethod
    def add_before(cls, node: Node, key: Any):
        new_node = Node(key)
        new_node.previous_pointer = node.previous_pointer
        new_node.next_pointer = node
        node.previous_pointer = new_node

    @classmethod
    def add_after(cls, node: Node, key: Any):
        new_node = Node(key)
        new_node.next_pointer = node.next_pointer
        new_node.previous_pointer = node
        node.next_pointer = new_node

    def erase(self, key: Any):
        if self.__not_empty():
            current_node = self.head

            if current_node.key == key:
                self.head = self.head.next_pointer

                if not self.head:
                    self.tail = None

            while True:
                if current_node.next_pointer.key == key:
                    break

                elif current_node.next_pointer is None:
                    raise KeyDoesNotExist()

                else:
                    current_node = current_node.next_pointer

            current_node.next_pointer = current_node.next_pointer.next_pointer.next_pointer

    def clear(self):
        self.head = None
        self.tail = None

    def empty(self) -> bool:
        if self.head:
            return False

        else:
            return True

    def find(self, key: Any) -> bool:
        if self.__not_empty():
            return self.head.find(key)

    def __not_empty(self):
        if self.head:
            return True

        else:
            raise ListEmptyException()