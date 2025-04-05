from dataclasses import dataclass
from typing import Any

from .node import Node
from ..exception.exceptions import ListEmptyException

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
    head: Node
    tail: Node

    def push_front(self, key: Any):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node

        if not self.tail:
            self.tail = self.head

    def push_back(self, key: Any):
        pass

    def top_front(self):
        pass

    def top_back(self):
        pass

    def pop_front(self):
        node = self.head
        self.head = node.next_pointer
        del node

    def pop_back(self, key: Any):
        pass

    def add_before(self, node: Node, key: Any):
        pass

    def add_after(self, node: Node, key: Any):
        pass

    def erase(self, key: Any):
        pass

    def empty(self) -> bool:
        pass

    def find(self):
        pass


@dataclass
class SinglyLinkedList:
    head: Node | None = None
    tail: Node | None = None

    def push_front(self, key: Any):
        new_node = Node(key)

        if self.head:
            new_node.next = self.head
            self.head = new_node

        else:
            self.head = new_node
            self.tail = new_node

    def push_back(self, key: Any):
        new_node = Node(key)

        if self.tail:
            self.tail.next = new_node
            self.tail = new_node

        else:
            self.head = new_node
            self.tail = new_node

    def top_front(self) -> Any:
        if self.head:
            return self.head.key

        else:
            raise ListEmptyException()

    def top_back(self) -> Any:
        if self.tail:
            return self.tail.key

        else:
            raise ListEmptyException()

    def pop_front(self):
        if self.head:
            if self.head != self.tail:
                next_pointer = self.head.next_pointer
                self.head = next_pointer

            else:
                self.head = self.head.next_pointer
                self.tail = self.head.next_pointer

        else:
            raise ListEmptyException()

    def pop_back(self, key: Any):
        if not self.head:
            raise ListEmptyException()

        if self.head == self.tail:
            self.head = None
            self.tail = None

        else:
            current_node = self.head

            while current_node.next_pointer != self.tail:
                current_node.next_pointer =


                else:
                    current_node = current_node.next_pointer

    def add_before(self, node: Node, key: Any):
        pass

    def add_after(self, node: Node, key: Any):
        pass

    def erase(self, key: Any):
        pass

    def empty(self) -> bool:
        if self.head:
            return True

        else:
            return False

    def find(self, key: Any) -> Node:
        if self.head:
            return self.head.find(key)

        else:
            raise ListEmptyException()