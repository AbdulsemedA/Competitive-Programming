# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ret= []
        while head:
            ret.append(head.val)
            head =  head.next
        ans = [0]*len(ret)
        stack = []
        for i,num in enumerate(ret):
            while stack and stack[-1][0] < num:
                p,idx = stack.pop()
                ans[idx] = num
            stack.append((num,i))
        return ans
