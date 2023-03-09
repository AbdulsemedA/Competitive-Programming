# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def combine(root1, root2):
            if not root1 and not root2: return None
            if root1 and not root2: return root1
            if root2 and not root1: return root2
            
            root1.left = combine(root1.left,root2.left)
            root1.right = combine(root1.right, root2.right)
            root1.val += root2.val
            
            return root1

        return combine(root1, root2)