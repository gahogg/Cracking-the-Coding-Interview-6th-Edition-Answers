# a) Implement an algorithm to determine if a string has all unique characters.
# b) What if you cannot use additional data structures?


# a) (With data structures)
# O(n) time, O(n) space
def is_unique_string_a(s):
    d = {}
    for letter in s:
        if letter in d:
            return False
        else:
            d[letter] = 1


    return True


# b) (Without data structures)
# O(n*log(n)) time, O(n) space
def is_unique_string_b(s):
    if len(s) == 1 or len(s) == 0:
        return True
    sorted_s = "".join(sorted(s))
    for i in range(len(sorted_s)-1):
        first = sorted_s[i]
        second = sorted_s[i+1]
        if first == second:
            return False

    return True


s1 = ""
s2 = "a"
s3 = "ab"
s4 = "bb"
s5 = "bab"
trues = [s1, s2, s3]
falses = [s4, s5]

assert all([is_unique_string_a(s) for s in trues])
assert all([is_unique_string_a(s) is False for s in falses])

assert all([is_unique_string_b(s) for s in trues])
assert all([is_unique_string_b(s) is False for s in falses])