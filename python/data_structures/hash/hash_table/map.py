
"""
load factor alpha = (n/m)
if 0.5 < alpha < 1
-alpha > 1 --> we have definitely collision
-alpha < 0.5 --> half of hash table is empty space and wasted memory
O(m) = O(n/alpha) = O(n) is memory usage complexity (our dynamic array cardinality)
O(1+alpha) is the speed of our hash table --> average O(1)
control amount of memory by m (cardinality)

** DYNAMIC Hash Table

Dynamic Hash table use the theory of dynamic array which it starts by a small cardinality (m) and dynamic array
and become bigger if the amount of alpha breaks the rules. (become too large)

we should use new hash function for new cardinality (m)

Rehashing: suppose to keep alpha below than 0.9

Rehashing time O(n) but amortization is O(1) like dynamic array

C++ --> unordered_map
Java --> HashMap
Python --> dict

"""

from python.data_structures.hash_table.hash_func import StringHashFunction
from python.data_structures.hash_table.map_key import MapKey
from python.data_structures.linked_lists.doubly import Node


from python.data_structures.array.array import DynamicArray
from python.data_structures.linked_lists import DoublyLinkedList


class HashTable:
    def __init__(self, cardinality: int = 1000):
        self.__bucket_size = cardinality
        self.__size = 0
        self.__chains: DynamicArray = self.__initialize() # slots \ buckets
        self.__hashing_func = StringHashFunction(cardinality)
        self.__alpha = self.__size / self.__bucket_size

    def __initialize(self) -> DynamicArray:
        chains = DynamicArray(self.__bucket_size)

        for _ in range(self.__bucket_size):
            chains.push_back(DoublyLinkedList())

        return chains

    def add(self, key, value):
        self.set(key, value)

    def pop(self, key):
        hashed_index = self.__hashing_func.hash(key)
        chain = self.__chains[hashed_index]
        chain.erase(hashed_index)
        self.__size -= 1

    def get(self, key, default=None):
        hashed_index = self.__hashing_func.hash(key)
        chain = self.__chains[hashed_index]

        for mapped_key in chain:
            if mapped_key == key:
                return mapped_key.value

        return default

    def set(self, key, value):
        self.__resize()
        hashed_index = self.__hashing_func.hash(key)

        print('Hashed index', hashed_index)

        chain = self.__chains[hashed_index]
        map_key = MapKey(key=key, value=value)

        for pair in chain:
            node: Node = pair.search(map_key)

            if node:
                node.key = map_key
                return

        chain.push_front(map_key)
        self.__size += 1
        self.__calculate_alpha()

    def has_key(self, obj) -> bool:
        hashed_index = self.__hashing_func.hash(obj)
        chain = self.__chains[hashed_index]

        for (key, value) in chain:
            if key == obj:
                return True

        return False

    def __resize(self):
        if self.__alpha < 0.9:
            return

        new_bucket_size = 2 * self.__bucket_size
        new_hash_func = StringHashFunction(new_bucket_size)
        new_chains = DynamicArray(new_bucket_size)

        for _ in range(new_bucket_size):
            new_chains.push_back(DoublyLinkedList())

        for index in range(self.__bucket_size):
            chain = self.__chains[index]
            for map_key in chain:
                encoded_index = new_hash_func.hash(map_key.key)
                new_chains[encoded_index].push_front(map_key)

        self.__chains = new_chains
        self.__bucket_size = new_bucket_size
        self.__hashing_func = new_hash_func

    def __calculate_alpha(self):
        self.__alpha = self.__size / self.__bucket_size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.set(key, value)
