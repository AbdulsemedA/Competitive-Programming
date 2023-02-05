# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size, count, temp = 1, 0, head
        curr = head
        
        while curr and curr.next:
            size += 1
            curr = curr.next

        k %= size
        
        if not k:
            return head
        
        while count < size - k:
            nextn = temp
            temp = temp.next
            count += 1
            
        nextn.next = None
        curr.next = head
        
        return temp
    
        