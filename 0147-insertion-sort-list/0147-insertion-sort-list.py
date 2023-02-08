# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        if not head.next:
            return head

        curr = head.next
        maxi = head
        
        while curr:
            before = dummy
            tmp = dummy.next
            
            if curr.val < maxi.val:
                while tmp.val < curr.val:
                    before = tmp
                    tmp = tmp.next
                    
                maxi.next = curr.next
                curr.next = before.next
                before.next = curr
                curr = maxi.next

            else:
                maxi = maxi.next
                curr = curr.next
        
        return dummy.next
                    
                    
                
        