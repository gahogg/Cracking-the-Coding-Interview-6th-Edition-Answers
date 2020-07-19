# Given a string, write a function to check if it is a permutation of a plaindrome. A plaindrome is a word or phrase
# that is the same forwards and backwards. A permutation is a rearrangement of letters, not limited to dictionary words.


# O(n) time, O(n) space
def is_palindrome_permutation(s):
    dic = {}

    # Get number of occurrences of each letter
    for letter in s:
        if letter in dic:
            dic[letter] += 1
        else:
            dic[letter] = 1

    seen_odd = False

    # Check if more than one letter has an odd number of occurrences
    for key in dic:
        if dic[key] % 2 == 0:
            continue
        else:
            if seen_odd:
                return False
            else:
                seen_odd = True

    return True


trues = ["a", "aa", "aab", "aabb", "aabbc", "aabbaa", "aabbaaccc"]
falses = ["ab", "accb", "aabbaaccde"]

assert all([is_palindrome_permutation(s) for s in trues])
assert all([is_palindrome_permutation(s) is False for s in falses])