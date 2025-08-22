arr = [0, 1, 0, 3, 12]
result= []
for i in arr:
    if i != 0:
        result.append(i)
zero_count= arr.count(0)           # count zeroes
result.extend([0] * zero_count)    # Add zeros at end
result