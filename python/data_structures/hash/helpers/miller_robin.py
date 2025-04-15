from random import randint


class MillerRobin:

    def find_next_prime(self, number):
        if number <= 2:
            return 2

        number = number + 1 if number % 2 == 0 else number + 2  # start with an odd number
        while not self.__is_prime(number):
            number += 2

        return number


    @classmethod
    def __is_prime(cls, n, k=5):  # Miller-Rabin Test
        if n <= 3:
            return n > 1
        if n % 2 == 0:
            return False

        r, d = 0, n - 1
        while d % 2 == 0:
            d //= 2
            r += 1

        for _ in range(k):
            a = randint(2, n - 2)
            x = pow(a, d, n)
            if x in (1, n - 1):
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True