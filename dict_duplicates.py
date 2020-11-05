def my_function():
    letters = input("Write the string: ")
    if letters == "":
        print("String is empty.")
    dc = {}
    for letter in letters:
        if dc.get(letter) is None:
            dc[letter] = 1
        else:
            dc[letter] += 1

    dt = {}

    for x, y in dc.items():
        if y > 1 and x != " ":
            dt[x] = y
            print(x, y)
    return dt


my_function()
