from python.data_structures.hash_table.hash_family.int import IntegerHashFunction
from python.data_structures.hash_table.hash_family.polynomial import PolynomialHashing


class StringHashFunction:
    def __init__(self, cardinality: int = 2, max_value: int = 10 ** 15):
        self.__cardinality = cardinality
        self.__integer_hash = IntegerHashFunction(max_value=max_value)
        self.__polynomial_hash = PolynomialHashing(max_value=max_value)

    def hash(self, string: str):
        hashed_str = self.__polynomial_hash.hash(string)
        hashed_integer = self.__integer_hash.hash(hashed_str)
        return hashed_integer % self.__cardinality

