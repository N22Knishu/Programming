class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def display(head):
    while head:
        print(head.data,end=",")
        head=head.next.next
head = Node(1)
head.next = Node(2)
display(head)
