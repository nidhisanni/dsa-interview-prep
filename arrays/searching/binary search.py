def binarysearch(arr, num):
    i= 0
    j= len(arr) - 1
    
    while i <= j:
        mid= (i+j) // 2
        
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            i= mid+1
        else:
            j= j-1
    return -1

nums= [1, 3, 5, 7, 9, 11, 13]
num = 7

result= binarysearch(nums, num)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")