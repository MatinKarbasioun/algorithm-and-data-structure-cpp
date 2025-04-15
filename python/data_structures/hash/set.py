from typing import Any

from python.data_structures.array.array import DynamicArray
from python.data_structures.linked_lists import DoublyLinkedList

"""
Real world use-cases

Students on campus
phone numbers of contacts
keywords in a programming language


C++ --> unordered_ser
Java --> HashSet
Python --> set

"""

class Set:
    def __init__(self):
        self.__bucket_size = 10
        self.__chains = self.__initialize() # slots \ buckets
        self.__hashing_func = HashFunction()

    def __initialize(self) -> DynamicArray:
        chains = DynamicArray(self.__bucket_size)
        for index in range(len(chains)):
            chains[index] = DoublyLinkedList()

        return chains

    def add(self, obj: Any):
        chain = self.__chains[self.__hashing_func.hash(obj)]

        if not chain.find(obj):
            chain.push_back(obj)

    def remove(self, obj: Any):
        if not self.find(obj):
            return

        chain = self.__chains[self.__hashing_func.hash(obj)]
        chain.erase(obj)

    def find(self, obj: Any):
        chain = self.__chains[self.__hashing_func.hash(obj)]

        for key in chain:
            if key == obj:
                return key

        return False
