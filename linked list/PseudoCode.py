

#traversal in linked list
class node:
    def __init__(self,data):
        self.data= data
        self.next= None
class SLL:
    def __init__(self):
        self.head= None
    def traversal(self):
        if self.head is None:
            print('singly linked list is empty')
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, "->",end="")
                temp=temp.next
            print("None")
sll = SLL()
head = node(6)  
sll.head = head
n1= node(7)
head.next = n1
n2= node(8)
n1.next = n2
n3= node(9) 
n2.next = n3     


sll.traversal()




