# linked list are collection of items where the first item is known as head and the last item is known as null. 
# Its very easy to add an item to a linked list 
# With the following Node we can create any kind of node 
# With any kind of data TYPE 
# https://www.youtube.com/c/AnthonySistilli

class listNode:
    def __init__(self,data):
        self.value= data
        self.next = None
# Lets create a linked list manually 
Node1=listNode(3)
Node2=listNode(7)
Node3=listNode(10)

Node1.next=Node2
Node2.next=Node3
Node3.next=None


print(Node1)  # This referes to the address of Node1 in memory
print(Node2)  # This referes to the address of Node2 in memory
print(Node3)  # This referes to the address of Node3 in memory 

print(f'{Node1.value}')
print(f'{Node2.value}')
print(f'{Node3.value}')
# Traversing the singly linked list having known the Node1
currentNode=Node1
while True:
    if currentNode==None:
        break
    print(f'{currentNode.value} "-->" ')
    currentNode=currentNode.next
    
    
    




    


    
    
        