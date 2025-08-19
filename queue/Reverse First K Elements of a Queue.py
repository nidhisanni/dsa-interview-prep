from collections import deque

def reverse_first_k(queue, k):
    if k>len(queue) or k<=0:
        return queue
    
    stack=[]
    
    for i in range(k):
        stack.append(queue.popleft())
    while stack:
        queue.append(stack.pop())
        
    size= len(queue)
    for i in range(size - k):
        queue.append(queue.popleft())
    return queue
q = deque([1, 2, 3, 4, 5])
k = 3
print("Original Queue:", list(q))
result = reverse_first_k(q, k)
print("Queue after reversing first K elements:", list(result))
