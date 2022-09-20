# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        while(head!=None):
            arr.append(head.val)
            head = head.next
        arr.pop(len(arr)-n)
        arr = arr[::-1]
        node = None
        for i in arr:
            node = ListNode(i,next=node)
        return node
