def generate_parentheses(open_p, close_p, s=""):
    if open_p == 0 and close_p == 0:
        print(s)
        return
    if open_p > 0:
        generate_parentheses(open_p-1, close_p, s+"(")
    if close_p > open_p:
        generate_parentheses(open_p, close_p-1, s+")")
