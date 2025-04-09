"""
Queue is FIFO (First in, First Out)

Real-world use cases:

Printing tasks in a printer
- documents are printed in the order they are received

Applications where the order of requests matters
- tickets for a concert
- taxi services

"""

from python.linked_lists import SinglyLinkedList


class Queue:
    def __init__(self):
        self.__size = 0
        self.__memory = SinglyLinkedList()

    def enqueue(self, key):
        self.__size += 1
        self.__memory.push_back(key)

    def dequeue(self):
        self.__size -= 1
        top = self.__memory.pop_front()
        return top

    def empty(self) -> bool:
        return self.__memory.empty()

    @property
    def size(self) -> int:
        return self.__size
