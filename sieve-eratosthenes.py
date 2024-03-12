# Implementation of the Sieve of Eratosthenes: a classic algorithm for finding all prime numbers up to a given limit n.
# The sieve_of_eratosthenes function initializes a list of numbers from 2 to n and iterates through the list, marking multiples of each prime number as non-prime.
# The remove_multiples function is responsible for removing those multiples.
# After the execution of the sieve_of_eratosthenes function, the list remaining contains the prime numbers up to n. 


def sieve_of_eratosthenes(n):
    from math import sqrt
    numbers = list(range(2, n + 1))
    i = 0
    while numbers[i] <= sqrt(n):
        remove_multiples(numbers, i)
        i += 1
    return numbers

def remove_multiples(numbers, i):
    el = numbers[i]
    for j in range(len(numbers) - 1, i, -1):
        if numbers[j] % el == 0:
            del numbers[j]

primes_up_to_60 = sieve_of_eratosthenes(60)
print(primes_up_to_60)
