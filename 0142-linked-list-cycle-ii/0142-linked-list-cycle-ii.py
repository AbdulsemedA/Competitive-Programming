# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        
        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if slow == fast:           
                if slow == head:
                    return slow
                
                slow = head

                while slow and fast:
                    slow = slow.next
                    fast = fast.next

                    if slow == fast:
                        return slow
                break
            
        return None
        