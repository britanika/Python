def find_max(numbers: list) -> int:
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    print(maximum)


num = [3, 5, 2, 7, 8]
find_max(num)
# Output: 8

