import sympy

# อ่านไฟล์และแปลงตัวเลขเป็นลิสต์
with open('primes_0-1000000.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]

# ตรวจสอบว่าตัวเลขทั้งหมดเป็นจำนวนเฉพาะหรือไม่
all_primes = all(sympy.isprime(number) for number in numbers)

print("All numbers are prime:", all_primes)