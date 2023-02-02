# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left == right: 
            return head
        
        dummy = ListNode()
        dummy.next = head
        before = dummy
        count = 0
        
        while before and before.next:
            if count == left - 1:
                break
                
            before = before.next
            count += 1
        
        prev = None
        curr = before.next
        count += 1
        
        while curr and curr.next:
            while count <= right:
                nextn = curr.next
                curr.next = prev
                prev = curr
                curr = nextn
                count += 1
                
            break
         
        before.next.next = curr
        before.next = prev
            
        return dummy.next