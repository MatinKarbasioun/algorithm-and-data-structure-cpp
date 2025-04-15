"""

compare P with all substring S of T of length |P|

P --> our search
S --> all substring in position T[i,i+|P|-1]
T --> target text

Idea:
use hashing to make the comparison faster

if h(P) != h(S) --> P != S
if h(P) = h(S) --> they are equal

check whether P = S or not

use polynomial hash family

if P != S --> the probability of the hash collision is |P|/p for polynomial hashing can be reduced by choosing
large prime number (p)


"false alarm" event is the event which raised when P is compared with S (substring of T), but P != S (but their hash
is the same) --> collision happened
collision come by alpha means (n/m)

Naive Algorithm: O(|T||P|)
"""
from python.data_structures.hash.hash_family.polynomial import PolynomialHashing


class RabinKarp:

    def check(self, text: str, substring: str) -> list[int]:
        hashing_funct = PolynomialHashing(len(substring) * len(text))

        for i in range(0, len(text) - len(substring) + 1):

            if 1 == 9:
                pass
