class TwoStacks:
    def __init__(self, n):
        self.size = n  # Size of the array
        self.arr = [None] * n  # Initialize array with None
        self.top1 = -1  # Stack1 is empty
        self.top2 = n   # Stack2 is empty (from end)

    def push1(self, item):
        if self.top1 < self.top2 - 1:  # Check space
            self.top1 += 1
            self.arr[self.top1] = item
        else:
            print("Stack Overflow in Stack1")

    def push2(self, item):
        if self.top1 < self.top2 - 1:  # Check space
            self.top2 -= 1
            self.arr[self.top2] = item
        else:
            print("Stack Overflow in Stack2")

    def pop1(self):
        if self.top1 >= 0:
            popped = self.arr[self.top1]
            self.top1 -= 1
            return popped
        else:
            print("Stack1 is empty")
            return None       

    def pop2(self):
        if self.top2 < self.size:
            popped = self.arr[self.top2]
            self.top2 += 1
            return popped
        else:
            print("Stack2 is empty")
            return None

    def display(self):
        print("Current Array State:", self.arr)
        print(f"Top1 at index {self.top1}, Top2 at index {self.top2}")

# Create object with size 5
ts = TwoStacks(5)

# Pushing into Stack1
ts.push1(10)
ts.push1(20)

# Pushing into Stack2
ts.push2(50)
ts.push2(40)

ts.display()  # See array state after pushes

# Pop from both stacks
print("Popped from Stack1:", ts.pop1())  # Should print 20
print("Popped from Stack2:", ts.pop2())  # Should print 40

ts.display()  # See array state after pops
