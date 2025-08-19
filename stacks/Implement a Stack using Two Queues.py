from collections import deque

class StacksUsingQueues:
    def __init__(self):
        self.queue1= deque()
        self.queue2= deque()
        
    def push(self, item):
        self.queue2.append(item)
        
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
            
        self.queue1, self.queue2 = self.queue2, self.queue1
        
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.queue1.popleft()
    
    def is_empty(self):
        return len(self.queue1)==0
    
    def display(self):
        print(list(self.queue1))
        
s= StacksUsingQueues()
s.push(1)
s.push(2)
s.push(3)
s.display()
print('popped:', s.pop())
s.display()