"""
STRONG NUMBER
A strong number is a number whose sum of factorials of digits equals the number itself.
Example: 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145
"""

def factorial(n):
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_strong_number(num):
    total = 0
    temp = num
    
    while temp > 0:
        digit = temp % 10
        total += factorial(digit)
        temp //= 10
    
    return total == num

# Test Cases
print("Strong Number Examples:")
numbers = [7, 8, 325, 30685, 567, 70]
for num in numbers:
    if is_strong_number(num):
        print(f"{num} is a Strong Number")
    else:
        print(f"{num} is NOT a Strong Number")
