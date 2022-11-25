"""
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.

Return the maximum number of points you can earn by applying the above operation some number of times.
"""

from collections import Counter


nums1 = [3,4,2]
"""
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.
"""

nums2 = [2,2,3,3,3,4]
"""
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.
"""

def deleteAndEarn(nums: list[int]) -> int:
    count = Counter(nums)
    nums = sorted(list(set(nums)))

    print(nums)
    print(count)

    coin1, coin2 = 0, 0

    for i in range(len(nums)):
        nowCoin = nums[i] * count[nums[i]]
        if nums[i] == nums[i - 1] + 1:
            tempCoin = max(coin2 ,nowCoin + coin1)
            coin1 = coin2
            coin2 = tempCoin
        else:
            tempCoin = nowCoin + coin2
            coin1 = coin2
            coin2 = tempCoin
    
    return coin2

print(deleteAndEarn(nums2))
