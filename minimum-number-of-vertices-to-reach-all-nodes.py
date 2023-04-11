class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        sink = [False for _ in range(n)]

        for src, des in edges:
            sink[des] = True

        return [i for i in range(len(sink)) if not sink[i]]