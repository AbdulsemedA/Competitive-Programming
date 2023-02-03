# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        
        fast = slow = temp = head
        count, middle = 1, 0
        
        while temp and temp.next:
            count += 1
            temp = temp.next
       
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            middle += 1
        
        if count % 2:
            middle += 1
       
        curr = head
        prev = None
        iters = 0
        
        while curr and curr.next:
            while iters < middle:
                nextn = curr.next
                curr.next = prev
                prev = curr
                curr = nextn
                iters += 1

            break
            
        if count % 2:
            prev = prev.next

        while prev:
            if prev.val != curr.val:
                return False
            
            prev = prev.next
            curr = curr.next
            
        return True
            
        
        
        