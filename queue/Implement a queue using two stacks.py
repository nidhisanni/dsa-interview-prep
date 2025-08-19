class QueueUsingTwoStacks:
    def __init__(self):
        self.stack1= []
        self.stack2= []
        
    def enqueue(self, item):
        self.stack1.append(item)
        print(f'enqueued {item}')
        
    def dequeue(self):
        if not self.stack2:
            if not self.stack1:
                print('queue is empty')
                return None
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        removed= self.stack2.pop()
        print(f'dequeued {removed}')
        return removed
    
    def peek(self):
        if not self.stack2:
            if not self.stack1:
                print('queue is empty')
                return None
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
     
    def is_empty(self):
        return not self.stack1 and not self.stack2
    
    def display(self):
            queue_list = self.stack2[::-1] + self.stack1
            print(f'current queue: {queue_list}')
        
q = QueueUsingTwoStacks()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

q.dequeue()
q.display()

