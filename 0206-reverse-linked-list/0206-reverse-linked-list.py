# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode()
        nextn = ListNode()
        current = ListNode()
        
        current = head
        prev = None
        
        while current:
            nextn = current.next
            current.next = prev
            prev = current
            current = nextn
            
        head = prev
        
        return head
        