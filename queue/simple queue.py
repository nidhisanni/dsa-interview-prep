# queue=[]

# #enqueue
# queue.append(1)
# queue.append(2)
# queue.append(3)

# print("queue after enqueue:", queue)99

# #dequeue
# front= queue.pop(1)
# print('dequeued element:',front)
# print('queue after dequeue:', queue)

class queue:
    def __init__(self):
        self.items=[]
        
    def enqueue(self,item):
        self.items.append(item)
        print(f'enqueued {item}')
        
    def dequeue(self):
        if not self.is_empty():
            removed= self.items.pop(0)
            print(f'dequeued {removed}')
            return removed
        else:
            print('queue is empty')
            return None
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print('queue is empty')
            return None
    def is_empty(self):
        return len(self.items)==0
    def display(self):
        print(f'current queue: {self.items}')
        
q= queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

print('front element is:', q.peek())

q.dequeue()
q.display()