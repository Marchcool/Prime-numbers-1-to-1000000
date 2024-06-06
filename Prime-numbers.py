def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if primes[p] is True:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, limit + 1) if primes[p]]
    return prime_numbers

def write_prime_numbers_to_file(prime_numbers, filename):
    with open(filename, 'w') as file:
        for prime in prime_numbers:
            file.write(str(prime) + '\n')

if __name__ == "__main__":
    limit = 1000000
    prime_numbers = sieve_of_eratosthenes(limit)
    write_prime_numbers_to_file(prime_numbers, 'prime_numbers.txt')
