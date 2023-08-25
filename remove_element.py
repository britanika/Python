# https://leetcode.com/problems/remove-element/
def remove_element(nums, val):
    if not nums:
        return 0

    new_nums = []
    for num in nums:
        if num != val:
            new_nums.append(num)
    nums[:] = new_nums
    k = len(nums)

    return k

# Example:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
