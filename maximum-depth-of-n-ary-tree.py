"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        Queue = deque([root])
        max_depth = 0

        while Queue:
            for _ in range(len(Queue)):
                node = Queue.popleft()

                for child in node.children:
                    Queue.append(child)

            max_depth += 1
        
        return max_depth