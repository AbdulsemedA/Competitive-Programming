# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.freq = {}
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root):
            if not root: return root
            inorder(root.left)
            self.freq[root.val] = 1 + self.freq.get(root.val, 0)
            inorder(root.right)
            return root
        inorder(root)
        maxi = max(self.freq.values())
        return [k for k,v in self.freq.items() if v == maxi]