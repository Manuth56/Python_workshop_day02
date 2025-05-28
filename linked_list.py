class Node:
    #Function to initialize the nodeobject
    def __init__(self,data):
        self.data= data #Assign data
        self.next=None #initialize next as null

#linked List class contain a Node object
class LinkedList:
#Function to initialize head
    def __init__(self):
        self.head=None

#print method
    def listprint(self):
        printval=self.head
        while printval is not None:
            print(printval.data)
            printval=printval.next

    def _insert_at_Begining(self,newdata):
        newNode=Node(newdata)
        newNode.next=self.head
        self.head=newNode

ll=LinkedList()
ll.head=Node("Toyoyta")
l2=Node("BMW")
l3=Node("Audi")
l4=Node("Lamborghini")
ll.head.next=l2
l2.next=l3
l3.next=l4
ll.listprint()

ll._insert_at_Begining("Chr")
print("")
ll.listprint()