# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        A_list = []
        total = []
        for i in lists:
            while i != None:
                A_list.append(i.val)
                i = i.next
        for i in A_list:
            total.append(i)
        total.sort(reverse=True)
        head = None
        for i in total:
            head = ListNode(i,next=head)
        return head
