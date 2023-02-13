# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        
        odds = connector = head
        even_head = ListNode(0,None)
        evens = even_head
        
        while odds and odds.next:
            newNode = ListNode(odds.next.val)
            evens.next = newNode
            evens = evens.next
            odds.next = odds.next.next
            connector = odds
            odds = odds.next
        
        if odds:
            odds.next = even_head.next
        else:
            connector.next = even_head.next
        
        return head
            
            
            
        