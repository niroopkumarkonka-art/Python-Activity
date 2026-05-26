"""
PALINDROME
A palindrome is a word/number that reads the same forwards and backwards.
Example: "racecar" is a palindrome, "hello" is not
"""

def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

# Test Cases
print("Palindrome Examples:")
words = ["racecar", "hello", "madam", "step on no pets", "level", "python"]
for word in words:
    if is_palindrome(word):
        print(f"'{word}' is a PALINDROME")
    else:
        print(f"'{word}' is NOT a PALINDROME")
