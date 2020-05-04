"""
Sieve of Eratosthenes -
It is a simple, ancient algorithm for finding all prime numbers up to any given limit.
It does so by iteratively marking as composite (i.e. not prime),
the multiples of each prime, starting with the multiples of 2.
"""


def se1():
    n = int(input("Enter the number(>1) up to which the prime has to be computed :- "))
    if n < 1:
        raise ValueError("The number entered must be greater than +1")
    primes = [x for x in range(2, n+1)]
    i = 0
    for num in primes:
        if num**2 > primes[-1]:
            break
        primes = primes[0:i]+list(filter(lambda x: x % num != 0, primes[i:]))
        i += 1
    print([2] + primes)


if __name__ == "__main__":
    se1()
