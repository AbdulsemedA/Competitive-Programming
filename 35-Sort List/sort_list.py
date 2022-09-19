# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        while head!=None:
            result.append(head.val)
            head = head.next
        result.sort(reverse=True)
        head = None 
        for i in result:
            head = ListNode(i, next=head)
        return head
