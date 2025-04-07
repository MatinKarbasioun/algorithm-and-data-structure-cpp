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
class SinglyLinkedList:
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
            self.head = self.head.next_pointer

            if not self.head:
                self.tail = None

    def pop_back(self):
        if self.__not_empty():
           if self.head == self.tail:
               self.head = None
               self.tail = None

           else:
               current_node = self.head

               while current_node.next_pointer.next_pointer:
                  current_node = current_node.next_pointer

               current_node.next_pointer = None
               self.tail.next_pointer = current_node

    def add_before(self, node: Node, key: Any):
        current_node = self.head

        if self.head == node:
           new_node = Node(key)
           new_node.next_pointer = self.head
           self.head = new_node

        else:
           new_node = Node(key)

           while True:
               if current_node.next_pointer == node:
                   break

               elif current_node.next_pointer is None:
                   raise NodeDoesNotExist()

               else:
                   current_node = current_node.next_pointer

           new_node.next_pointer = current_node.next_pointer
           current_node.next_pointer = new_node

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
            return True

        else:
            return False

    def find(self, key: Any) -> bool:
        if self.__not_empty():
            return self.head.find(key)

    def __not_empty(self):
        if self.head:
            return True

        else:
            raise ListEmptyException()