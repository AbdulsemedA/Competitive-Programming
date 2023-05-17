class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = set()

        for i in edges:
            src, des = i
            graph[src].append(des)
            graph[des].append(src)
        
        stack = [source]

        while stack:
            node = stack.pop()
            if node == destination: return True
            visited.add(node)

            for child in graph[node]:
                if child not in visited:
                    stack.append(child)

        return False