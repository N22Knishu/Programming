# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
      
        while(head != None and head.val == val):
            head = head.next
        if head is None:
            return None
        curPointer = head
        prev = curPointer
        while(curPointer != None and curPointer.next != None ):
            if(curPointer.next.val == val ):
                toLink = curPointer.next.next
                while(toLink is not None and toLink.val ==val):
                    toLink = toLink.next
                curPointer.next =toLink
            prev = curPointer
            curPointer=curPointer.next
        if(curPointer == val):
            prev.next=None
        return head