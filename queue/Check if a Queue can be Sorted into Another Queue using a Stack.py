from collections import deque

def can_sort_queue(input_q, output_q):
    stack=[]
    
    input_q= deque(input_q)
    output_q= deque(output_q)
    
    while input_q:
        if input_q[0]== output_q[0]:
            input_q.popleft()
            output_q.popleft()
        else:
            stack.append(input_q.popleft())
    
    while stack:
        if stack[-1]== output_q[0]:
            stack.pop()
            output_q.popleft()
        else:
            return False
        
    return True
input_queue= [2,3,1]
output_queue=[2,1,3]   #“Sorted” = can we achieve the target sequence using the stack rules?

print('Can sort using stack?', can_sort_queue(input_queue, output_queue))
    