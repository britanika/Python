# def is_anagram(s1, s2) -> bool:
# return sorted(s1) == sorted(s2) # O(nlogn)

def is_anagram(s1, s2) -> bool:
    # Remove spaces and convert to lowercase to make the comparison case-insensitive and space-insensitive.
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # Check if the lengths are equal. If not, they cannot be anagrams.
    if len(s1) != len(s2):
        return False

    # Initialize a dictionary to count character frequencies in s1.
    char_count = {}

    # Count the character frequencies in s1.
    for char in s1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Compare the character frequencies in s2.
    for char in s2:
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
        else:
            return False

    return True  # O(n)


# Test cases
print(is_anagram("listen-", "silent-"))  # True
print(is_anagram("hello", "world"))  # False
print(is_anagram("hello", "olleh"))  # True
print(is_anagram("anagram!", "nagaram!"))  # True
print(is_anagram("rag", "car"))  # False
