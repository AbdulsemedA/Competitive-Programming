# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.paths = []

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def travel(root, curr):
            if not root:
                return root
            curr.append(str(root.val))
            left = travel(root.left, curr)
            right = travel(root.right, curr)
            if not root.left and not root.right:
                self.paths.append('->'.join(curr))
                curr.pop()
                return
            curr.pop()
            
        path = travel(root, [])
        return self.paths