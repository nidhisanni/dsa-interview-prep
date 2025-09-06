def fibo_no(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return fibo_no(n-1) + fibo_no(n-2)

print(fibo_no(4))
        