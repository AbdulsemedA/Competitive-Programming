# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sums = 0

        def dfs(node):
            nonlocal sums
            if not node: return
            if node.left:
                if not node.left.left and not node.left.right:
                    sums += node.left.val
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return sums
