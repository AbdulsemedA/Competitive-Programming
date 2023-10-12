# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def flip(R1, R2):
            if not R1 and not R2:
                return True

            if not R1 or not R2 or R1.val != R2.val:
                return False
    
            return (flip(R1.left, R2.left) and flip(R1.right, R2.right) or 
                flip(R1.left, R2.right) and flip(R1.right, R2.left))
        
        return flip(root1, root2)