# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = half = maxi = 0
        curr = first = second = head
        before, prev = second, None
        
        while curr:
            curr = curr.next
            n += 1
       
        while half < (n // 2):
            before = second
            second = second.next
            half += 1
        
        while second:
            nextn = second.next
            second.next = prev
            prev = second
            second = nextn
        
        before.next = None
        
        while prev:
            maxi = max(maxi, prev.val + head.val)
            prev = prev.next
            head = head.next
        
        return maxi
            