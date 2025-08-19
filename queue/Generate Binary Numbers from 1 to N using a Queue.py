from collections import deque

def GenerateBinaryNumbers(n):
    q= deque()
    
    q.append("1")
    
    result=[]
    
    for i in range(n):
         # Step 1: Dequeue front element
        front = q.popleft()
        result.append(front)
        
                # Print current step
        print(f"Step {i+1}:")
        print("Output so far:", result)
        print("Queue before enqueue:", list(q))
        
                # Step 2: Enqueue front+"0" and front+"1"
        q.append(front + "0")
        q.append(front + "1")

        print("Queue after enqueue:", list(q))
        print("-" * 40)

    return result


# Example
nums = GenerateBinaryNumbers(5)
print("Final Binary Numbers:", nums)

