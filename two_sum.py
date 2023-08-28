#https://leetcode.com/problems/two-sum/
def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    output = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                output.append(i)
                output.append(j)
                return output

# Example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

