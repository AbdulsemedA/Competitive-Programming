# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.Sub = False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def preorder(root,Big):
            if not root: return [None]
            curr = [str(root.val)] + preorder(root.left,Big) + preorder(root.right, Big)
            if Big and curr == subTree:
                self.Sub = True           
            return curr
        subTree = preorder(subRoot, 0)
        full = preorder(root,1)
        return self.Sub