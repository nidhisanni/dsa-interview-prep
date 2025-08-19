class stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None 
    def is_empty(self):
        return len(self.items)==0
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
    def is_balanced(expression):
        s=stack()
        for ch in expression:
            if ch in '({[':
                s.push(ch)
            elif ch in ')}]':
                if s.is_empty():
                    return 'not balanced'
                top=s.pop()
                
                if (ch==')' and top != '(' or (ch == ']' and top != '[') or (ch == '}' and top != '{')):
                    return 'not balanced'
                    
        if s.is_empty():
            return 'balanced'
        else:
            return 'not balanced'            
expr = "{[()]}"
print(stack.is_balanced(expr))  

expr2 = "{[(])}"
print(stack.is_balanced(expr2))  