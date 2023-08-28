
letters = input("Write the string: ")
duplicates = []
for i in range(0, len(letters)):
    counter = 1
    for j in range(i + 1, len(letters)):
        if letters[i] == letters[j] and letters[i] != ' ':
            counter = counter + 1
    if counter > 1 and letters[i] not in duplicates:
        duplicates.append(letters[i])


print(f'Duplicates in string are: {duplicates}')

