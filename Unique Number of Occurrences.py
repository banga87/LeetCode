"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.
"""

from collections import Counter

def uniqueOccurrences(arr: list[int]) -> bool:
    map = Counter(arr)
    return len(list(map.values())) == len(set(map.values()))

arr = [-3,0,1,-3,1,1,1,-3,10,0]

print(uniqueOccurrences(arr))