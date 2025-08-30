class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LL:
    def __init__(self):
        self.head = None
        
    def traverse(bothself):
        if self.head is None:
            print('empty ll')
            return
        else:
            current = self.head
            while current is not None:
                print(current.data, end='->')
                current = current.next
            print('none')
            
    def insert_at_beginning(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node
        
    def length(self):
        count = 0
        current = self.head
        while current is not None:
            
            current = current.next 
            count += 1
        return count

ll = LL()
ll.insert_at_beginning(30)
ll.insert_at_beginning(20)
ll.insert_at_beginning(10)

ll.traverse()

print('length:' , ll.length())
