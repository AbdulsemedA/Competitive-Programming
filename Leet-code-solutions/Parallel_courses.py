from collections import defaultdict, deque

def parallelCourses(n, prerequisites):
    graph = defaultdict(list)
    degree = defaultdict(int)
    queue = deque()
    mini_sem = count = 0

    for src, des in prerequisites:
        graph[src].append(des)
        degree[des] += 1
       
    for ele in range(1, n + 1):
        if not degree[ele]:
            queue.append(ele)

    while queue:
        size = len(queue)
        mini_sem += 1
        count += size
        
        for _ in range(size):
            curr = queue.popleft()
            
            for ele in graph[curr]:
                degree[ele] -= 1

                if not degree[ele]:
                    queue.append(ele)
    
    return mini_sem if count == n else -1
