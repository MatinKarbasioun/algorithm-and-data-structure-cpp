from random import randint
import numpy as np

from python.data_structures.hash.hash_family.polynomial import PolynomialHashing
from python.data_structures.hash.helpers.miller_robin import MillerRobin


class HashingRecurrence:
    def __init__(self, max_value):
        self.__prime = MillerRobin().find_next_prime(max_value)
        self.__x = randint(1, self.__prime-1)
        self.__polynomial_hash = PolynomialHashing(max_value)

    def calculate(self, string):
        encoded_str = np.zeros(len(string))
        hashed_value = np.zeros(len(string))

        for i in range(len(string)):
            encoded_str[i] = ord(string[i])

        for i in range(len(string) - 1, -1, -1):
            hashed_value[i] = 1
