
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


"""
from python.data_structures.hash_table.hash_func import StringHashFunction
from python.data_structures.hash_table.map_key import MapKey

"""

C++ --> unordered_map
Java --> HashMap
Python --> dict

"""
from python.data_structures.array.array import DynamicArray
from python.data_structures.linked_lists import DoublyLinkedList


class HashTable:
    def __init__(self, cardinality: int = 1000):
        self.__bucket_size = cardinality
        self.__size = 0
        self.__chains = self.__initialize() # slots \ buckets
        self.__hashing_func = StringHashFunction(cardinality)
        self.__alpha = self.__size / self.__bucket_size

    def __initialize(self) -> DynamicArray:
        chains = DynamicArray(self.__bucket_size)

        for index in range(len(chains)):
            chains[index] = DoublyLinkedList()

        return chains

    def add(self, key, value):
        self.__size += 1
        map_key = MapKey(key=key, value=value)
        encoded_index = self.__hashing_func.hash(key)
        if encoded_index < len(self.__chains):
            self.__chains[encoded_index].add(key, value)

        else:
            self.__chains.push_back(DoublyLinkedList()).add(key, value)

    def pop(self, obj):
        encoded_index = self.__hashing_func.hash(obj)
        chain = self.__chains[encoded_index]
        chain.pop(encoded_index)

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
