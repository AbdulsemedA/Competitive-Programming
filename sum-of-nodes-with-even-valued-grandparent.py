# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.size = 0
        self.total = 0
        
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def travel(root, curr):
            if not root:
                return root
            curr.append(root.val)
            print(curr)
            self.size += 1
            left = travel(root.left, curr)
            right = travel(root.right, curr)
            if not root.left and not root.right:
                if self.size >= 3:
                    if curr[-3] % 2 == 0:
                        self.total += curr[-1]
                curr.pop()
                self.size -= 1
                return
            if self.size >= 3:
                if curr[-3] % 2 == 0:
                    self.total += curr[-1]
            curr.pop()
            self.size -= 1
            
        path = travel(root, [])

        return self.total