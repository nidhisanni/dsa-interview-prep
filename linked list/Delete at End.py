class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LL:
    def __init__(self):
        self.head = None
        
    def traverse(self):
        a = self.head
        if a is None:
            print('empty')
            return
        else:
            while a is not None:
                print(a.data, end='->')
                a = a.next
            print('none')
            
    def insert_at_beginning(self, data):
        new_node = node(data)         # 1. Create a new node with the given data
        new_node.next = self.head     # 2. Point new node’s 'next' to the current head
        self.head = new_node
            
    def delete_at_end(self):
        a = self.head
        if self.head is None:
            print('list is empty')
            return
        else:
            while a.next.next is not None:
                a= a.next
            a.next = None
            
ll = LL()
ll.insert_at_beginning(20)
ll.insert_at_beginning(30)
ll.insert_at_beginning(40)
ll.traverse()

ll.delete_at_end()
ll.traverse()