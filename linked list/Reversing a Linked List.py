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
    
    #iterative method
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            
            current.next = prev
            
            prev = current 
            current = next_node 
        self.head = prev
        
     # Recursive reverse
    def reverse_recursive(self, head):
        # Base case: empty list or single node
        if head is None or head.next is None:
            return head

        # Step 1: reverse the rest of the list
        new_head = self.reverse_recursive(head.next)

        # Step 2: fix the link
        head.next.next = head
        head.next = None

        return new_head
    
ll= linkedlist()
ll.insert_at_beginning(20)
ll.insert_at_beginning(30)
ll.insert_at_beginning(40)

ll.traverse()
ll.reverse()
ll.traverse()

ll.head = ll.reverse_recursive(ll.head)
ll.traverse() 