# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(start, end):
            if start > end:
                return None
            mid = start + (end - start) // 2
            node = TreeNode(nums[mid])
            node.left = build(start, mid - 1)
            node.right = build(mid + 1, end)
            return node
        return build(0, len(nums) - 1)