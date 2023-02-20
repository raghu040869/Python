
def valid_anagram(s, t):
    if len(s) != len(t):
        return False
    for c in s:
        if s.count(c) != t.count(c):
            return False
    return True


print(valid_anagram("anagram", "nagaram"))
print(valid_anagram("rat", "car"))
