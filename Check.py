import sympy

with open('primes_0-1000000.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]

all_primes = all(sympy.isprime(number) for number in numbers)

print("All numbers are prime:", all_primes)
