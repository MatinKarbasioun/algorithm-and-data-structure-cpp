from python.array.array import DynamicArray
from python.hash_table.hash_func import HashFunction
from python.linked_lists import DoublyLinkedList
from python.linked_lists.doubly import Node

"""

C++ --> unordered_map
Java --> HashMap
Python --> dict

"""
class HashMap:
    def __init__(self):
        self.__bucket_size = 10
        self.__chains = self.__initialize() # slots \ buckets
        self.__hashing_func = HashFunction()

    def __initialize(self) -> DynamicArray:
        chains = DynamicArray(self.__bucket_size)
        for index in range(len(chains)):
            chains[index] = DoublyLinkedList()

        return chains

    def add(self, key, value):
        encoded_index = self.__hashing_func.hash(key)
        if encoded_index < len(self.__chains):
            self.__chains[encoded_index].add(key, value)

        else:
            self.__chains.push_back(DoublyLinkedList()).add(key, value)

    def get(self, obj, default=None):
        encoded_index = self.__hashing_func.hash(obj)
        chain = self.__chains[encoded_index]

        for (key, value) in chain:
            if key == obj:
                return value

        return default

    def set(self, obj, value):
        encoded_index = self.__hashing_func.hash(obj)

        chain = self.__chains[encoded_index]

        for pair in chain:
            node: Node = pair.search((obj, value))

            if node:
                node.key = (obj, value)
                return

        chain.append((obj, value))

    def has_key(self, obj) -> bool:
        encoded_index = self.__hashing_func.hash(obj)
        chain = self.__chains[encoded_index]

        for (key, value) in chain:
            if key == obj:
                return True

        return False

    def __getitem__(self, key):
        return self.get(key)
