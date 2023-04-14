# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0

        def allPath(root, nums):
            nonlocal total
            if not root: return

            if not root.left and not root.right:
                nums.append(str(root.val))
                total += int(''.join(nums))
                return

            allPath(root.left, nums + [str(root.val)])
            allPath(root.right, nums + [str(root.val)])
            
        allPath(root, [])

        return total