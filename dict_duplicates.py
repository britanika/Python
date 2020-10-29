def my_function():
    letters = input("Write the string: ")
    dc = {}
    for letter in letters:
        if dc.get(letter) is None:
            dc[letter] = 1
        else:
            dc[letter] += 1

    for x, y in dc.items():
        if y > 1 and x != " ":
            print(x, y)


my_function()
