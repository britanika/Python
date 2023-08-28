# https://leetcode.com/problems/merge-sorted-array/
def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    while nums1 and nums1[-1] == 0:
        nums1.pop()
    merged_array = []
    for num in nums1:
        merged_array.append(num)
    for num in nums2:
        merged_array.append(num)

    merged_array = sorted(merged_array)
    k = len(merged_array)
    while k < m + n:
        merged_array.append(0)
        k = k + 1
    nums1[:] = merged_array

    return nums1

# Example :
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
