"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
"""

s1 = 'paper'
t1 = 'title'
s2 = 'foo'
t2 = 'bar'
s3 = 'egg'
t3 = 'add'
s4 = 'badc'
t4 = 'baba'

def isIsomorphic(s, t) -> bool:
    dict = {c : 0 for c in s}
    for i in range(len(s)):
        if dict[s[i]] == 0 and t[i] not in dict.values():
            dict[s[i]] = t[i]
        if dict[s[i]] != t[i]:
            return False
    return True

print(isIsomorphic(s1, t1))
print(isIsomorphic(s2, t2))
print(isIsomorphic(s3, t3))
print(isIsomorphic(s4, t4))