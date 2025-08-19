class stack:
    def __init__(self):
        self.items=[]
        
    def push(self, item):
        self.items.append(item)
        print(f'Pushed {item}, current stack: {self.items}' )
        
    def pop(self):
        if not self.is_empty():
            removed= self.items.pop()
            print(f'Popped {removed}, current stack: {self.items}' )
        else:
            print('Stack is empty, nothing to pop.')

    def peek(self):
        if not self.is_empty():
            print(f'Peeked at stack, top item: {self.items[-1]}')
            return self.items[-1]
        else:
            print('Stack is empty, nothing to peek.')
            
    def is_empty(self):
        return len(self.items) == 0
    def display(self):
        print(f'Current stack: {self.items}')
        
s = stack()
s.push(1)
s.push(2)
s.push(3)
s.display()
s.peek()
s.pop()
s.display()
s.peek()