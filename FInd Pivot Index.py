"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""

nums1 = [1,7,3,6,5,6]
nums2 = [1,2,3]
nums3 = [2,1,-1]

def pivotIndex(nums) -> int:
    total = sum(nums)
    leftSum = 0
    for i in range(len(nums)):
        rightSum = total - nums[i] - leftSum
        if leftSum == rightSum:
            return i
        leftSum += nums[i]
    return -1

print(pivotIndex(nums1))
print(pivotIndex(nums2))
print(pivotIndex(nums3))
# print(sum(nums3[0+1:]))

