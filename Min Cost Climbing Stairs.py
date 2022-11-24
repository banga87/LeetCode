"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.
"""

def minCostClimbingStairs(cost: list[int]) -> int:
    if len(cost) == 1:
        return cost[0]
    if len(cost) == 2:
        return min(cost[0], cost[1])

    for i in range(2, len(cost)):
        cost[i] += min(cost[i - 1], cost[i - 2])

    print(cost)
    return min(cost[-1], cost[-2])

arr1 = [10, 15, 20, 1]
arr2 = [1,100,1,1,1,100,1,1,100,1]

min_cost = minCostClimbingStairs(arr2)
print(min_cost)