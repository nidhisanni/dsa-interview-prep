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
    def display(self):
        return self.items
    
s= stack()
input_string= 'hello'

for ch in input_string:
    s.push(ch)
    
print('stack contents:', s.display())

reversed_string=''
while not s.is_empty():
    ch = s.pop()
    print(f"Popped: {ch}")
    reversed_string = reversed_string + ch

print('reversed string:', reversed_string)

