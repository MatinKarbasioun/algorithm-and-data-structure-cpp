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


class HashFunction:
    @classmethod
    def hash(cls, value) -> str:
        pass

