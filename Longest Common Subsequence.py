"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
"""

def longestCommonSubsequence(text1: str, text2: str) -> int:
    def dp(i, j):

        if i < 0 or j < 0:
            return 0

        if text1[i] == text2[j]:
            return 1 + dp(i - 1, j - 1)
        elif i == 0:
            return dp(i, j - 1)
        else:
            return dp(i - 1, j)

    return dp(len(text1) - 1, len(text2) - 1)

t1 = "psnw"
t2 = "vozsh"

print(longestCommonSubsequence(t1, t2))