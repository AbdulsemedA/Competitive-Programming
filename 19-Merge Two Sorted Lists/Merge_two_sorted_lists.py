# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        while list1 != None:
            result.append(list1.val)
            list1 = list1.next
        while list2 != None:
            result.append(list2.val)
            list2 = list2.next
        result.sort(reverse=True)
        head = None
        for x in result:
            head = ListNode(x, next=head)
        return head
