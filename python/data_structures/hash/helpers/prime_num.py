def find_first_prime_less_than_number(number):

    if number % 2 == 0:
        number -= 1

    for candidate in range(number, 2, -2):
        for divisor in range(3, int(candidate ** 0.5) + 1, 2):
            if candidate % divisor == 0:
                break
        else:
            return candidate

    return 3

def find_first_prime_bigger_than_number(number):
    candidate = number

    while True:

        for divisor in range(3, int(candidate ** 0.5) + 1, 2):
            if candidate % divisor == 0:
                break

        else:
            return candidate

        candidate += 2
