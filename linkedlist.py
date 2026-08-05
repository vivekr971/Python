class Node:
    def __init__ (self,val):
        self.val=val
        self.next=None
            
# node1=Node(5)
# node2=Node(10)
# node3=Node(7)
# node4=Node(8)

# node1.next=node2
# node2.next=node3
# node3.next=node4

# print(node1.val)

class SinglyLinkedList:
    def __init__(self):
        self.head=None
        
    def append(self,data):
        new_node=Node(data)
        
        if not self.head:
            self.head=new_node
        else:
            current=self.head
            
            while current.next is not None:
                current=current.next
                
            current.next=new_node
            
    def traverse(self):
        
        if not self.head:
            print("SLL is empty")
            
        else:
            current=self.head
            
            while current is not None:
                print(current.val, end="")
                current=current.next
                print()
                
sll= SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.traverse()

'''
    def insert_at(self,val,position):
        new_node=Node(val)
        if position==0:
            new_node.next=self.head
            self.head=new_node
        else:
            prev_node=None
            current=self.head
            count=0
            
            while current is not None and count<position:
                prev_node=current
                current=current.next
                count+=1
            prev_node.next=new_node
            new_node.next=current

'''
            
            
            
            