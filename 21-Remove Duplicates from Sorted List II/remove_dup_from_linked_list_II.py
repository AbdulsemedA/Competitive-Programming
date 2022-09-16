# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        while head != None:
            res.append(head.val)
            head = head.next
        res.sort(reverse=True)
        result = []
        for i in res:
            if i not in result and res.count(i) == 1:
                result.append(i)
        temp = None
        for x in result:
            temp = ListNode(x, next=temp)
        return temp
