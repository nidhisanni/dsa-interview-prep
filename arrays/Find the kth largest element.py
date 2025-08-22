arr = [3, 2, 1, 5, 6, 4]
k=3
arr.sort(reverse= True)  #  Sort in decreasing order
print('sorted array:', arr)

kth_largest= arr[k-1]
print(f'{k}th largest element is:', kth_largest)  #This f is called an f-string, or formatted string literal. We use it to easily include variables inside strings.
