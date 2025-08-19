def sort_stack(input_stack):
    temp_stack=[]
    
    while input_stack:
        temp = input_stack.pop()
        
        while temp_stack and temp_stack[-1]> temp:
            input_stack.append(temp_stack.pop())
            
        temp_stack.append(temp)
        
    while temp_stack:
        input_stack.append(temp_stack.pop())
        
    return input_stack

stack = [1, 5, 2, 4, 3]
print("Original Stack (Top to Bottom):", stack[::-1])

sorted_stack = sort_stack(stack)

print("Sorted Stack (Top to Bottom):", sorted_stack[::-1])
