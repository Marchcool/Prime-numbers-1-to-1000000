def check_prime_numbers(filename):
    with open(filename, 'r') as file:
        prime_numbers = [int(line.strip()) for line in file]
    return prime_numbers

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    filename = 'prime_numbers.txt'
    prime_numbers = check_prime_numbers(filename)
    for prime in prime_numbers:
        if not is_prime(prime):
            print(f"{prime} is not a prime number!")
