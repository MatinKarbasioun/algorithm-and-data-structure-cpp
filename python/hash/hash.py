import numpy as np


class HashTable:
    def __init__(self):
        self.__default_size = 10
        self.__buckets = np.array([]) # slots

    def add(self, key, value):
        pass

    def get(self, key):
        pass

    def __getitem__(self, key):
        return self.get(key)
