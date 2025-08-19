from collections import deque

def first_unique(queue):
    freq={}
    
    for num in queue:
        freq[num]= freq.get(num, 0) + 1
        
    for num in queue:
        if freq[num]==1:
            return num
        
    return None

q = deque([4, 5, 1, 2, 0, 4])
print("Queue:", list(q))
print("First Unique Element:", first_unique(q))
