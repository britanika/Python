numbers = [2, 3, 6, 1, 2, 5, 1, 4, 3, 5]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)


