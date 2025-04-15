"""
Our hash function should have these properties:
1- be fast enough in looking up
2- has a small possibility of collision
3- has a small number of cardinality m

map:
phone number --> name of contact
name of contact --> phone number

map from set S of objects to set of V of values
is data structure with methods HashKey(object)
and Get(object), Set(object, value), where objects belonging S, value belonging to V

map S to V ==> S: set of keys, V: set of values

Chaining:
1- select hash function h of cardinality m (small cardinality)
2- create array chains of size m
3- each element of chains is a doubly-linked list of pairs (name, phone number), called chain
4- pair (name, phone number) goes into chain at position h(key) in the array Chains (find corresponding index)

if we want to look up name by phone number, go to the chain corresponding to phone number and look
through all pairs

"""
from random import randint

from python.data_structures.hash_table.helpers.miller_robin import MillerRobin
from python.data_structures.hash_table.helpers.prime_num import find_first_prime_less_than_number, \
    find_first_prime_bigger_than_number

"""
if cardinality equal to 1000
if there is a function to generate randomly between 0 to 999, so we have a uniform distributions
but hash function should be repetitive and we can find the same random number as we hash it again

So hash function should be:
 1- deterministic
 2- fast to compute
 3- distribute keys well into different celss
 4- few collisions 

the simple one for phone numbers:
h(x) = ((a * x + b) mod p) mode p

1 <= a <= p-1
0 <= b <= p-1
p > our import values (maybe phone numbers should be bigger than 10 digits number)
"""

class IntegerHashFunction:
    def __init__(self, max_value: int):
        self.__prime = MillerRobin().find_next_prime(max_value)
        self.__a = randint(1, self.__prime - 1)
        self.__b = randint(0, self.__prime - 1)

    def hash(self, value) -> int:
        return (self.__a * value + self.__b) % self.__prime
