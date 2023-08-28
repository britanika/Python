# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
def remove_duplicates(nums):
    if not nums:
        return 0

    unique_elements = []

    for num in nums:
        if num not in unique_elements:
            unique_elements.append(num)

    for i in range(len(unique_elements)):
        nums[i] = unique_elements[i]

    return len(unique_elements)

# Example:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
