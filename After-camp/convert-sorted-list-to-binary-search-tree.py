# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        def build(start, end):
            if start > end:
                return None
            mid = start + (end - start) // 2
            node = TreeNode(nums[mid])
            node.left = build(start, mid - 1)
            node.right = build(mid + 1, end)
            return node
        return build(0, len(nums) - 1)