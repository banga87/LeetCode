"""
You are given two 0-indexed integer arrays nums and multipliers of size n and m respectively, where n >= m.
You begin with a score of 0. You want to perform exactly m operations. On the ith operation (0-indexed) you will:
Choose one integer x from either the start or the end of the array nums.
Add multipliers[i] * x to your score.
Note that multipliers[0] corresponds to the first operation, multipliers[1] to the second operation, and so on.
Remove x from nums.
Return the maximum score after performing m operations.
"""


from functools import lru_cache

numbers = [-5,-3,-3,-2,7,1]
multis = [-10,-5,3,4,6]

def maximumScore_topDown(nums: list[int], multipliers: list[int]) -> int:
    
    @lru_cache(2000)
    def dp(i , left):
        # Base Case
        if i == m:
            return 0

        multi = multipliers[i]
        right = n - 1 - (i - left)

        # Recurrance Relation
        return max(
            multi * nums[left] + dp(i + 1, left + 1),
            multi * nums[right] + dp(i + 1, left)
            )

    n, m = len(nums), len(multipliers)

    return dp(0,0)


def maximumScore_bottomUp(nums: list[int], multipliers: list[int]) -> int:
    n, m = len(nums), len(multipliers)

    dp = [0] * (m + 1)

    for i in range(m - 1, -1, -1):
        for left in range(i + 1):
            multi = multipliers[i]
            right = n - 1 - (i - left)
            dp[left] = max(
                multi * nums[left] + dp[left + 1],
                multi * nums[right] + dp[left]
                )

    return dp[0]


print(maximumScore_bottomUp(numbers, multis))
print(maximumScore_topDown(numbers, multis))