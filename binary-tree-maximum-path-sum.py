# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = float('-inf')

        def allPath(node):
            nonlocal maxi
            if not node: return 0

            Left = max(0, allPath(node.left))
            Right = max(0, allPath(node.right))

            maxi = max(maxi, Left + Right + node.val)
            return node.val + max(Left, Right)

        allPath(root)
        return maxi