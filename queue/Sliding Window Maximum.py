from collections import deque

def sliding_window_max(arr,k):
    n= len(arr)
    
    if n*k ==0:
        return[]
    if k==1:
        return arr
    
    d= deque()
    result=[]
    
    for i in range(n):
        if d and d[0]==i-k:
            d.popleft()
        while d and arr[d[-1]]< arr[i]:
            d.pop()
            
            d.append(i)
            
            if i>=k-1:
                result.append(arr[d[0]])  # front of deque = max
    
    return result

# Example
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_max(arr, k))