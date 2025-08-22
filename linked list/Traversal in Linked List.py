class node:
    def __init__(self, data):
        self.data= data
        self.next= None
        
class linkedlist:
    def __init__(self):
        #When the list is created, it’s empty, so head is None
        self.head= None
            
    def traverse(self):
        if self.head is None:
            print('linked list is empty')
            return
        else:
            current= self.head
            while current is not None:
                print(current.data, end='->')
                current= current.next
            print('None')
ll= linkedlist()

n1= node(1)
n2= node(2)
n3= node(3)

# Link nodes together
n1.next= n2
n2.next= n3

#assign head
ll.head= n1
 #traverse the list
ll.traverse()          
                