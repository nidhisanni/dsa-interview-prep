class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LL:
    def __init__(self):
        self.head = None
        
    def traverse(self):
        if self.head is None:
            print('linked list is empty')
            return
        else:
            a= self.head
            while a is not None:
                print(a.data, end='->')
                a= a.next
            print('none')
            
    def insert_at_position(self, data, pos):
        new_node= node(data)
        
        #case1 : insert at beginning
        if pos==1:
            new_node.next= self.head
            self.head= new_node
            return
        
        #case2 : insert somewhere else
        a= self.head
        for i in range(1, pos - 1):
            if a is None:
                print('position out of range')
                return
            a = a.next
            
        if a is None:
            print('postion out of range')
            return
        
        new_node.next = a.next
        a.next = new_node
        
ll= LL()
ll.insert_at_position(20,1)
ll.insert_at_position(30,2)
ll.insert_at_position(10,2)
ll.traverse()