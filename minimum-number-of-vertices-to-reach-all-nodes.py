class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        sources = []
        src_snk = [[False, False] for _ in range(n)]

        for edge in edges:
            src, des = edge
            src_snk[src][0] = True
            src_snk[des][1] = True

        for i in range(len(src_snk)):
            if src_snk[i][0] and not src_snk[i][1]:
                sources.append(i)
        
        return sources