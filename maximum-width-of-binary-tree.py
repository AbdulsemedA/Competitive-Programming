# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        maxi = 0
        L = deque([(root, 0)])
        size, prev = 1, 0

        while L:
            prev = size
            left = L[0][1]
            for i in range(size):
                node, place = L.popleft()
                if node.left:
                    L.append((node.left, 2 * place))
                    size += 1
                if node.right:
                    L.append((node.right, 2 * place + 1))
                    size += 1
            size -= prev     
            maxi = max(maxi, place - left + 1)
            
        return maxi