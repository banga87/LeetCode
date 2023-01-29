"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

input of [-1,0,3,5,9,12]
target of 9 = 9
target of 2 = -1

"""

input1 = [-1,0,3,5,9,12]

# We split the list into two parts (high, low) and check where the middle index is in relation to the target value

def search(nums: list[int], target: int) -> int:
    low = 0
    mid = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] < target:
            low = mid + 1

        elif nums[mid] > target:
            high = mid - 1

        else:
            return nums[mid]

    return -1


print(search(input1, 9))
print(search(input1, 2))