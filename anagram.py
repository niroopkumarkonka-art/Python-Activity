"""
ANAGRAM
Two strings are anagrams if they contain the same characters with the same frequencies.
Example: "listen" and "silent" are anagrams
"""

def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1) == sorted(str2)

# Test Cases
print("Anagram Examples:")
pairs = [("listen", "silent"), ("hello", "world"), ("latent", "talent"), ("evil", "vile")]
for str1, str2 in pairs:
    if is_anagram(str1, str2):
        print(f"'{str1}' and '{str2}' are ANAGRAMS")
    else:
        print(f"'{str1}' and '{str2}' are NOT ANAGRAMS")
