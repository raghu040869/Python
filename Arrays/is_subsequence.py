# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
# of the characters without disturbing the relative positions of the remaining characters.
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
def is_subsequence(s , t):
    print(s, t)
    subsequence = 0
    if len(s) >= len(t): return False
    if len(s) == 0: return False
    for i in range(0, len(t)):
        if s[subsequence] == t[i]:
            subsequence += 1
    print(subsequence)
    return subsequence == len(s)


print(is_subsequence("ace", "abcde"))
print(is_subsequence("axc", "abcde"))
print(is_subsequence("aec", "abcde"))
print(is_subsequence("aaaaaa", "bbaaaa"))
print(is_subsequence("twn", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxtxxxxxxxxxxxxxxxxxxxxwxxxxxxxxxxxxxxxxxxxxxxxxxn"))
print(is_subsequence("ab", "baab"))
#