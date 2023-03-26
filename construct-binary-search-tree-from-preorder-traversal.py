# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        if not n:
            return None
        k = 1
        while k < n and preorder[k] < preorder[0]:
            k += 1
        
        left = self.bstFromPreorder(preorder[1:k])
        right = self.bstFromPreorder(preorder[k:])

        return TreeNode(preorder[0], left, right)