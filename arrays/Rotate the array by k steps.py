arr = [1, 2, 3, 4, 5, 6, 7]     #sloved using SLICING
k = 9
#New array = last k elements + first n - k elements
n= len(arr)
k = k % n  # In case k > n
rotated_arr = arr[-k: ] + arr[ :-k]
print("Rotated array:", rotated_arr)