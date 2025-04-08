"""
Real Use: Undo Functionallity
- push each keystroke
- pop last inserted keystroke

Symbol checker:
check the opening and closing of brackets and parentheses in ide
- push opening symbols
- check closing symbols
- pop matching opening symbols

Function calls
- push block of memory
- pop after the execution ends

Stacks are LIFO Queue (Last in, First Out)

"""
from python.linked_lists import SinglyLinkedList


class Stack:
    def __init__(self):
        self.__size = 0
        self.__memory = SinglyLinkedList()

    def push(self, key):
        self.__size += 1
        self.__memory.push_front(key)

    def top(self):
        return self.__memory.top_front()

    def peek(self):
        return self.__memory.top_front()

    def pop(self):
        self.__size -= 1
        top = self.__memory.pop_front()
        return top

    def empty(self) -> bool:
        return self.__memory.empty()

    @property
    def size(self) -> int:
        return self.__size
