def fibonacci(n: int) -> list[int]:
    fib_sequence: list[int] = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence  # O(n)

# print(fibonacci(10))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
