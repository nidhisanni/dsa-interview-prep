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
            
    def delete_at_pos(self, pos):
        a = self.head
        if self.head is None:
            print('list is empty')
            return
        
        if pos == 1:
            self.head = self.head.next
            return
        else:
            a = self.head
            for i in range(1, pos - 1):
                if a is None or a.next is None:
                    print('position out of range')
                    return
                a = a.next
                
            # Now a points to (pos-1)th node
            # a.next is the node to delete
            a.next = a.next.next
            
ll = LL()
ll.insert_at_beginning(20)
ll.insert_at_beginning(30)
ll.insert_at_beginning(40)
ll.traverse()
ll.delete_at_pos(4)
ll.traverse()