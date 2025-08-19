class stack:
    def __init__(self):
        self.items=[]
        
    def push(self, item):
        self.items.append(item)
        print(f'pushed {item} to the stack')
        
    def pop(self):
        if not self.is_empty():
            removed= self.items.pop()
            print(f'popped {removed} from the stack')
        else:
            print('stack is empty')
            
    def peek(self):
        if not self.is_empty():
            print(f'top item is {self.items[-1]}')
        else:
            print('stack is empty')
            
    def is_empty(self):
        return len(self.items)==0
    def display(self):
        print(f'current stack:{self.items}')
        
        
s= stack()
s.push(5)
s.push(10)
s.push(15)
s.pop()
s.peek()
s.display()