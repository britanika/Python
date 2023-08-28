# https://leetcode.com/problems/majority-element/description/
def majority_element(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    return nums[len(nums) // 2]

# Example:
# Input: nums = [3,2,3]
# Output: 3
