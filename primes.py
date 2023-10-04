"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if number_of_primes <= 0:
        raise ValueError

    if number_of_primes == 1:
        return [2]

    counter = 2
    while len(list) < number_of_primes:

        isPrime = True
        for prime in list:
            if counter % prime == 0:
                isPrime = False

        if isPrime:
            list.append(counter)
        counter += 1

    return list
