# Prime number checker - by [Charbel Hankache]
import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:  # 2 is special case
        return True
    if n % 2 == 0:  # Even numbers aren't prime (except 2)
        return False
    
    # Check up to square root
    max_divisor = math.isqrt(n) + 1  # +1 to include floor value
    for i in range(3, max_divisor, 2):  # Skip even numbers
        if n % i == 0:
            return False
    return True

# Testing (like a beginner would do)
print("2 is prime?", is_prime(2))     # Should be True
print("7 is prime?", is_prime(7))     # True
print("9 is prime?", is_prime(9))     # False
print("1 is prime?", is_prime(1))     # False