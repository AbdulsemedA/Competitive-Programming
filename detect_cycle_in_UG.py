from typing import List

class Solution:
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		color = [0] * V

        def hasCycle(parent, node):
            color[node] = 1
            
            for i in adj[node]:
                if not color[i]:
                    if hasCycle(node, i):
                        return True
                        
                elif i != parent:
                    return True
                    
            return False
        
        for i in range(V):
            if not color[i]:
                if hasCycle(-1, i):
                    return True
                    
        return False