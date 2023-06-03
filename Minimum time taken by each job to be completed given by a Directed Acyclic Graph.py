from collections import defaultdict, deque
from typing import List

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        answer = ["0"] * n
        
        for start, end in edges:
            graph[start].append(end)
            indegree[end] += 1
        
        queue = deque()
        
        for index in range(1, n+1):
            if indegree[index] == 0:
                queue.append(index)
        
        count = 1
        
        while queue:
            length = len(queue)
            
            for _ in range(length):
                node = queue.popleft()
                answer[node - 1] = str(count)
                
                for child in graph[node]:
                    indegree[child] -= 1
                    
                    if indegree[child] == 0:
                        queue.append(child)
            
            count += 1
        
        return " ".join(answer)


#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
   