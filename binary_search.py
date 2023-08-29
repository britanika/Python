# Binary Search Algorithm
def binary_search(arr, target):
    arr = sorted(arr)
    low = 0
    high = len(arr) - 1
    # Repeat until the pointers low and high meet each other
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Example usage:
arr = [2, 4, 6, 8, 10]
target = 4
result = binary_search(arr, target)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Element is not present in array")
# Output: Element is present at index 1
