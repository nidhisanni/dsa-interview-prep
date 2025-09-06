def calculate_sum(n):
    if n == 0 :
        return 0

    return calculate_sum(n-1) + n
print(calculate_sum(5))