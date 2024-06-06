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

def write_summary_to_file(prime_numbers, result_filename):
    correct_count = 0
    incorrect_count = 0

    for prime in prime_numbers:
        if is_prime(prime):
            correct_count += 1
        else:
            incorrect_count += 1

    total_count = correct_count + incorrect_count
    if total_count > 0:
        accuracy = (correct_count / total_count) * 100
    else:
        accuracy = 0

    with open(result_filename, 'w') as result_file:
        result_file.write(f"Total correct: {correct_count}\n")
        result_file.write(f"Total incorrect: {incorrect_count}\n")
        result_file.write(f"Accuracy: {accuracy:.2f}%\n")

if __name__ == "__main__":
    filename = 'prime_numbers.txt'
    result_filename = 'prime_check_summary.txt'
    prime_numbers = check_prime_numbers(filename)
    write_summary_to_file(prime_numbers, result_filename)
