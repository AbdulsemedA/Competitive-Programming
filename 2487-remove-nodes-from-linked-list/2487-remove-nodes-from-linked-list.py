# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        
        while curr:
            Nex = curr.next
            curr.next = prev
            prev = curr
            curr = Nex
        
        head = prev
        curr = head
        maxi = 0
        
        newHead = None
        
        while curr:
            if maxi <= curr.val:
                maxi = curr.val
                newHead = ListNode(curr.val, newHead)
            
            curr = curr.next
            
        return newHead
                
        
        
        