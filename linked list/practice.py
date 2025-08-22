class node:
    def __init__(self, data):
        self.data= data
        self.next= None

class SLL:
    def __init__(self):
        self.head = None
    def insertBeforeHead(self,data):      
        