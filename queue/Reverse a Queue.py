# Queue class (your version)
class queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.append(item)
        print(f'enqueued {item}')
        
    def dequeue(self):
        if not self.is_empty():
            removed = self.items.pop(0)
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
        return len(self.items) == 0

    def display(self):
        print(f'current queue: {self.items}')


# ---------- Q1: Reverse a Queue ----------

# Method 1: Using Stack
def reverse_queue_stack(q):
    stack = []              # temporary storage
    while not q.is_empty():
        stack.append(q.dequeue())
    for item in stack:
        q.enqueue(item)

# Method 2: Using Recursion
def reverse_queue_recursion(q):
    if q.is_empty():
        return
    item = q.dequeue()
    reverse_queue_recursion(q)
    q.enqueue(item)


# ---------- Example Run ----------
q = queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.display()

print("\n--- Using Stack ---")
reverse_queue_stack(q)
q.display()

print("\n--- Using Recursion ---")
reverse_queue_recursion(q)
q.display()
