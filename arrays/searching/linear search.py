def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

nums= [1,2,3,7,5,0,4]
target = 0

result= linear_search(nums, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
