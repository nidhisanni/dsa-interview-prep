class node:
    def __init__(self, data):
        self.data= data
        self.next= None
        
class linkedlist:
    def __init__(self):
        self.head= None
        
    def traverse(self):
        if self.head is None:
            print('linked list is empty')
            return
        else:
            current= self.head
            while current is not None:
                print(current.data, end= ' -> ')
                current= current.next
            print('none')
            
    def insert_at_beginning(self, data):
        new_node = node(data)         # 1. Create a new node with the given data
        new_node.next = self.head     # 2. Point new node’s 'next' to the current head
        self.head = new_node          # 3. Move head to point to the new node
        
ll= linkedlist()
ll.insert_at_beginning(20)
ll.insert_at_beginning(30)
ll.insert_at_beginning(40)

ll.traverse()
        