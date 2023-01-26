"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
"""

string = "abccccdddd"

def longestPalindrome(string) -> int:
    length = 0
    chars = {}
    for c in string:
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1

    for count in chars.values():
        if count > 1 and count % 2 == 0:
            length += count
        if count > 1 and count % 2 != 0:
            length += count - 1

    if len(string) > length:
        length += 1
    
    return length

    




longestPalindrome(string)


