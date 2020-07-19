# Given two strings, write a method to decide if one is a permutation of the other,


# O(n) time, O(n) space
def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    dic = {}

    for char in str1:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1

    for char in str2:
        if char not in dic:
            return False
        else:
            dic[char] -= 1

    for key in dic:
        if dic[key] != 0:
            return False

    return True


trues = [("hi", "hi"), ("hi", "ih"), ("ih", "hi"), ("long_one", "ne_logon")]
falses = [("is", "i"), ("is", "ki"), ("long_one", "long_ong")]

assert all([is_permutation(*strings) for strings in trues])
assert all([is_permutation(*strings) is False for strings in falses])