#User function Template for python3
from collections import defaultdict, deque

class Solution:
    def findOrder(self, array, N, K):
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for i in range(N - 1):
            word1 = array[i]
            word2 = array[i + 1]
            
            for w1, w2 in zip(word1, word2):
                if w1 != w2:
                    graph[w1].append(w2)
                    indegree[w2] += 1
                    break
        
        visited = set()
        queue = deque()
        answer = []
        
        for i in range(97, 97 + K):
            if not indegree[chr(i)]:
                queue.append(chr(i))
        
        while queue:
            curr = queue.popleft()
            answer.append(curr)
            
            for child in graph[curr]:
                indegree[child] -= 1
                
                if not indegree[child]:
                    queue.append(child)
        
        result = "".join(answer)
        
        return result
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends