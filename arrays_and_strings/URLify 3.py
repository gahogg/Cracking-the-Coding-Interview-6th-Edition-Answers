# Write a method to replace all spaces in a string with '%20'.


# O(n) time, O(n) space
def urlify(s, l):
    ret_s = ""
    for i, char in enumerate(s):
        if i > l - 1:
            break
        if char == " ":
            ret_s += "%20"
        else:
            ret_s += char
    return ret_s


ins = [("hi", 2), ("h i", 3), ("i hate you fwe", 10)]
outs = ["hi", "h%20i", "i%20hate%20you"]

assert all([urlify(*inp) == outp for inp, outp in zip(ins, outs)])