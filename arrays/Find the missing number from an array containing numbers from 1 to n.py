arr = [1, 2, 4, 5, 6]
n=6
total_sum = n * (n+1) / 2   # single slash / always returns a float, even if numbers are whole.
actual_sum= sum(arr          # double slash // means integer (floor) division.
missing_number= total_sum - actual_sum
print('the missing num is:', missing_number)

arr.append(missing_number)
arr.sort()
print("New array with missing number:", arr)