# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total = 0

        def travel(root, curr):
            nonlocal total

            if not root: return
            curr.append(root.val)

            left = travel(root.left, curr)
            right = travel(root.right, curr)

            if len(curr) >= 3:
                if curr[-3] % 2 == 0:
                    total += curr[-1]
            curr.pop()
            
        travel(root, [])

        return total