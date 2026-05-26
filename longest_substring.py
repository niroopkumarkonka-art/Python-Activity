"""
LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
Find the longest substring that doesn't contain duplicate characters.
Example: "abcabcbb" -> "abc" (length 3)
"""

def longest_substring(s):
    char_index = {}
    max_length = 0
    start = 0
    
    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1
        
        char_index[s[end]] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length

# Test Cases
print("Longest Substring Without Repeating Characters:")
strings = ["abcabcbb", "bbbbb", "pwwkew", "au", "dvdf", "abcdefgh"]
for s in strings:
    length = longest_substring(s)
    print(f"'{s}' -> Length: {length}")
