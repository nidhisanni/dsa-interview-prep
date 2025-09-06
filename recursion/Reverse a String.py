def reverse_string(s):
    if len(s) == 0:   # base case
        return ""
    return reverse_string(s[1:]) + s[0]
print(reverse_string("nidhi"))