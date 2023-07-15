class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        d = {}
        components = defaultdict(list)
    
        def find(x):
            d.setdefault(x, x)
            if d[x] != x:
                d[x] = find(d[x])
            return d[x]
    
        def union(x, y):
            s1 = find(x)
            s2 = find(y)
            d[s2] = s1
    
        for swap in allowedSwaps:
            union(swap[0], swap[1])
    
        for k, v in d.items():
            if k == v: components[k].append(k)
            else:
                parent = find(v)
                components[parent].append(k)
        
        visited = set()
        ham_dist = 0
    
        for comp, mem in components.items():
            srcDict = defaultdict(int)
            targetDict = defaultdict(int)
        
            for idx in mem:
                visited.add(idx)
                srcDict[source[idx]] += 1
                targetDict[target[idx]] += 1
            
            common = sum(min(srcDict[k], targetDict[k]) for k in srcDict.keys() if k in targetDict)
            ham_dist += len(mem) - common
        
        ham_dist += sum(source[i] != target[i] for i, v in enumerate(source) if i not in visited)
    
        return ham_dist