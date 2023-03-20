# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def travel(root, ans, L):
            if not root: return L
            if len(self.ans) < L + 1:
                self.ans.append([root.val])
            else:
                self.ans[L].append(root.val)

            travel(root.left, ans, L + 1)
            travel(root.right, ans, L + 1)

        travel(root, self.ans, 0)
        return [i[-1] for i in self.ans]