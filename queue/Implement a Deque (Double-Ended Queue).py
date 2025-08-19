# A deque is a queue where you can insert and remove elements from both ends — front and rear.
# Supports operations:
# append(x) → insert at rear
# appendleft(x) → insert at front
# pop() → remove from rear
# popleft() → remove from front
# peek_front() → check front element
# peek_rear() → check rear element
from collections import deque

class MyDeque:
    def __init__(self):
        self.d = deque()
    
    def append(self, x):
        self.d.append(x)
        print(f"Appended {x} at rear")
    
    def appendleft(self, x):
        self.d.appendleft(x)
        print(f"Appended {x} at front")
    
    def pop(self):
        if self.d:
            removed = self.d.pop()
            print(f"Popped {removed} from rear")
            return removed
        else:
            print("Deque is empty")
            return None
    
    def popleft(self):
        if self.d:
            removed = self.d.popleft()
            print(f"Popped {removed} from front")
            return removed
        else:
            print("Deque is empty")
            return None
    
    def peek_front(self):
        if self.d:
            return self.d[0]
        return None
    
    def peek_rear(self):
        if self.d:
            return self.d[-1]
        return None
    
    def display(self):
        print("Current Deque:", list(self.d))

# Example
dq = MyDeque()
dq.append(10)
dq.append(20)
dq.appendleft(5)
dq.display()
dq.pop()
dq.popleft()
dq.display()
print("Front:", dq.peek_front())
print("Rear:", dq.peek_rear())
