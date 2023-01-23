"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

s1 = 'abc'
t1 = 'ahbgdc'
s2 = 'axc'
t2 = 'ahbgdc'

def isSubsequence(s, t) -> bool:
    char1 = s[0]
    char2 = t[0]
    pointer = 0
    if len(s) == 0 or len(t) == 0:
        return False
    for i in range(len(t)):
        char2 = t[i]
        if char1 == char2 and pointer == len(s) - 1:
            return True
        elif char1 == char2:
            pointer += 1
            char1 = s[pointer]
    return False
      
print(isSubsequence(s1, t1))
print(isSubsequence(s2, t2))
