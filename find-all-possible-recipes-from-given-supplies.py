class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        queue = deque()
        supplies = set(supplies)
        graph = defaultdict(list)
        indegree = defaultdict(int)
        created = set()

        for i in range(len(recipes)):
            for j in range(len(ingredients[i])):
                if ingredients[i][j] not in supplies:
                    graph[ingredients[i][j]].append(recipes[i])
                    indegree[recipes[i]] += 1
                    
            if not indegree[recipes[i]]:
                queue.append(recipes[i])
        
        while queue:
            curr = queue.popleft()
            created.add(curr)

            for ele in graph[curr]:
                indegree[ele] -= 1
                if not indegree[ele]:
                    queue.append(ele)
        
        return created