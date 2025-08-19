from collections import deque

def interleaveQueue(queue):
    n = len(queue)
    half_size= n//2
    
    first_half= deque()
    for i in range(half_size):
        first_half.append(queue.popleft())
        
    while first_half:
        queue.append(first_half.popleft())
        
        queue.append(queue.popleft())
    return queue

q = deque([1, 2, 3, 4, 5, 6])
print("Original Queue:", list(q))

result = interleaveQueue(q)
print("Interleaved Queue:", list(result))
