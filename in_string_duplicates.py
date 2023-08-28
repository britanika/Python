from collections import Counter

letters = input("Write the string: ")
cnt = Counter(letters)

for key, value in cnt.items():
    if value >= 1 and key != " ":
        print(key, value)