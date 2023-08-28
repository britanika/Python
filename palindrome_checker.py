import re


def palindrome_checker(string) -> bool:
    pattern = r'[, /-]'  # This regular expression matches all the characters that we want to remove from the string
    modified_string = re.sub(pattern, '', string).lower()
    return modified_string[::-1] == modified_string


print(palindrome_checker("ana"))  # Output: True

print(palindrome_checker("A man, a plan, a canal-Panama"))  # Output: True
