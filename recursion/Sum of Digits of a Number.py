def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digits(n//10)     #// throws away the decimal part.
    
print(sum_of_digits(123))