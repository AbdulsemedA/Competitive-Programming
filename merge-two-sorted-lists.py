# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        if list1.val <= list2.val:
            merged = list1
            merged.next = self.mergeTwoLists(list1.next, list2)
        else:
            merged = list2
            merged.next = self.mergeTwoLists(list1, list2.next)

        return merged