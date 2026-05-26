"""
REMOVE DUPLICATES WITHOUT BUILT-IN FUNCTIONS
Remove duplicate elements from a list without using set() or other built-in functions.
Example: [1, 2, 2, 3, 3, 3] -> [1, 2, 3]
"""

def remove_duplicates(lst):
    result = []
    for item in lst:
        found = False
        for element in result:
            if item == element:
                found = True
                break
        if not found:
            result.append(item)
    return result

def remove_duplicates_string(s):
    result = []
    for char in s:
        found = False
        for c in result:
            if char == c:
                found = True
                break
        if not found:
            result.append(char)
    return ''.join(result)

# Test Cases
print("Remove Duplicates from List:")
lists = [[1, 7, 7, 8, 8, 8], [9, 9, 9, 5, 5, 2], [1, 2, 3], ['a', 'b', 'a', 'c']]
for lst in lists:
    result = remove_duplicates(lst)
    print(f"{lst} -> {result}")

print("\nRemove Duplicates from String:")
strings = ["aabbcc", "hello", "programming", "aaa"]
for s in strings:
    result = remove_duplicates_string(s)
    print(f"'{s}' -> '{result}'")
