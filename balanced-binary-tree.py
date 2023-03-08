# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.status = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def max_depth(root):
            if not root: 
                return 0    
            left = 1 + max_depth(root.left)
            right = 1 + max_depth(root.right)

            if abs(right - left) > 1:
                self.status = False
        
            return max(left,right)

        dpth = max_depth(root)
        return self.status