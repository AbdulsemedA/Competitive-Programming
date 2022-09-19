# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = []
        while l1!=None:
            n1.append(l1.val)
            l1 = l1.next
        n2 = []
        while l2!=None:
            n2.append(l2.val)
            l2 = l2.next
        n1.reverse()
        n2.reverse()
        num1 = int("".join(map(str, n1)))
        num2 = int("".join(map(str, n2)))
        final = num1 + num2
        digits = [int(x) for x in str(final)]
        # digits.reverse()
        head = None
        for i in digits:
            head = ListNode(i,next=head)
        return head
        
