arr=[12,89,45,67,90]
max_val= arr[0]
min_val= arr[0]
for i in arr:
    if i>max_val:
        max_val=i
    if i<min_val:
        min_val=i
print(max_val)
print(min_val)