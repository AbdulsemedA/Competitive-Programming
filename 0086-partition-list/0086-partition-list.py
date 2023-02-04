# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = less_tail = ListNode(0)
        greater_head = greater_tail = ListNode(0)
        curr = head
        
        while curr:
            if curr.val < x:
                less_tail.next = curr
                less_tail = less_tail.next
            else:
                greater_tail.next = curr
                greater_tail = greater_tail.next
                
            curr = curr.next
            
        greater_tail.next = None
        less_tail.next = greater_head.next
        
        return less_head.next

        