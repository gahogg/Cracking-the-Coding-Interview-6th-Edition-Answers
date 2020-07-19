# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace
# a character. Given two strings, write a function to check if they are one edit (or zero edits) away,


# O(n) time, O(1) space
def is_one_away(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    if l1 == l2:
        return s1 == s2
    if abs(l1 - l2) != 1:
        return False
    smaller_str = s1 if l1 < l2 else s2
    larger_str = s1 if l1 > l2 else s2
    smaller_len = len(smaller_str)
    small_ind = 0
    large_ind = 0
    error = False
    while small_ind < smaller_len:
        large_letter = larger_str[large_ind]
        small_letter = smaller_str[small_ind]
        if large_letter != small_letter:
            if error:
                return False
            else:
                error = True
        else:
            small_ind += 1
        large_ind += 1
    return True


trues = [("hi", "hi"), ("pale", "pal"), ("pale", "pal"), ("pale", "ale"), ("", "a")]
falses = [("pal", "pul"), ("pal", "pule"), ("long_one", "long_ong")]

assert all([is_one_away(*strings) for strings in trues])
assert all([is_one_away(*strings) is False for strings in falses])