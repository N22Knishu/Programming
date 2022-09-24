class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head=None
    def insertAtStart(self,data):
        node = Node(data)
        if self.head is None:
            self.head=node
            return
        node.next=self.head
        self.head=node
    def insertAtend(self,data):
        node = Node(data)
        point = self.head     
        #if self.head ==None:
        while point.next is not None:
            point=point.next
        point.next=node
    def removeNodeAtStart(self):
        if self.head is None:
            print("Empty list")
        else:
            self.head=self.head.next
    def removeNodeAtEnd(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            if self.head.next is None:
                self.head=None
            else:
                temp = self.head
                while temp.next.next is not None:
                    temp=temp.next
                lastNode=temp.next
                temp.next=None
                lastNode=None
    def display(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
sll = LinkedList()
sll.insertAtStart(10)
sll.insertAtStart(20)
sll.insertAtStart(80)
sll.insertAtend(90)
sll.removeNodeAtStart()
sll.removeNodeAtStart()
sll.removeNodeAtStart()
sll.removeNodeAtStart()
sll.removeNodeAtStart()
sll.removeNodeAtEnd()
sll.display()
       


        
        