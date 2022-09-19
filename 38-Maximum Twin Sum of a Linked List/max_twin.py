# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        result = []
        maxi = 0
        while head!=None:
            result.append(head.val)
            head = head.next
        for i in range(int(len(result)/2)):
            if result[i] + result[len(result)-i-1] > maxi:
                maxi = result[i] + result[len(result)-i-1]
        return maxi
        
