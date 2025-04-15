from random import randint

from python.data_structures.hash.helpers.miller_robin import MillerRobin


class PolynomialHashing:
    def __init__(self, max_value: int):
        self.__prime = MillerRobin().find_next_prime(max_value)
        self.__x = randint(1, self.__prime-1)

    def hash(self, string: str):
        hash_value = 0

        for i in range(len(string) - 1, -1, -1):
            hash_value = (hash_value * self.__x + ord(string[i])) % self.__prime

        return hash_value
