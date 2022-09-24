class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head=None
        self.lenLL=0
    def isEmpty(self):
        return self.head == None   
    def insertAtStart(self,data):
        node = Node(data)
        self.lenLL=self.lenLL+1
        if self.head is None:
            self.head=node
            return
        node.next=self.head
        self.head=node
    def insertAtend(self,data):
        
        node = Node(data)
        point = self.head
        self.lenLL=self.lenLL+1
        while point.next is not None:
            point=point.next
        point.next=node
    def removeNodeAtStart(self):
        if self.head is None:
            print("Empty list")
        else:
            self.head=self.head.next
            self.lenLL=self.lenLL-1
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
            self.lenLL=self.lenLL-1
            
    
    def removeNodeAtPos(self,pos):
        #case 0 : pos is 1 ~ remove head
        if(self.isEmpty()):
          print("No nodes to remove")
        if(pos>self.lenLL):
          return "Not enough nodes"  
        if(pos == 0):
            head = head.next
            return
        temp=self.head
        cnt=0
        while temp.next is not None:
            if(cnt+1==pos):
                temp.next = temp.next.next
                break
            temp=temp.next
            cnt=cnt+1
        self.lenLL=self.lenLL-1
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print()
        print("Length of the LinkedList",self.lenLL) 
sll = LinkedList()
sll.insertAtStart(10)
sll.insertAtStart(20)
sll.insertAtStart(80)
sll.insertAtStart(100)
sll.insertAtend(90)
sll.display()
sll.removeNodeAtPos(3)
sll.removeNodeAtStart()
sll.display()
       


        
        