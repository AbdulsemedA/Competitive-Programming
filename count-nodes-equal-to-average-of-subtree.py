# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def average(root):
            if not root:
                return [0,0]
            left = average(root.left)
            right = average(root.right)
            sums = left[0] + right[0] + root.val
            sizes = left[1] + right[1] + 1

            if sums // sizes == root.val:
                self.count += 1
            return [sums, sizes]
        average(root)
        return self.count