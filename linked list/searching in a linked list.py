class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LL:
    def __init__(self):
        self.head = None
        
    def traverse(self):
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
        
    def search(self, key):
        current = self.head
        pos = 1    # positions start at 1

        while current is not None:
            if current.data == key:
                return pos  # key found at this position

            current = current.next
            pos += 1
        return -1    # key not found

ll = LL()
ll.insert_at_beginning(30)
ll.insert_at_beginning(20)
ll.insert_at_beginning(10)

ll.traverse()

print(ll.search(20))
print(ll.search(10))