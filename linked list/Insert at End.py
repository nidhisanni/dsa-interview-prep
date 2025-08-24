class node:
    def __init__(self, data):
        self.data= data
        self.next= None
        
class LL:
    def __init__(self):
        self.head= None
    
    def traverse(self):
        if self.head is None:
            print('linked list is empty')
            return None
        else:
            current = self.head
            while current is not None:
                print(current.data, end=' -> ')
                current= current.next
            print('none')
            
    def insert_at_end(self, data):
        new_node= node(data)
        if self.head is None:     # case: empty list
            self.head= new_node
            return
        current= self.head
        while current.next is not None:
            current= current.next
        current.next= new_node
        
ll = LL()

# insert at end
ll.insert_at_end(30)
ll.insert_at_end(40)

ll.traverse()
            
            