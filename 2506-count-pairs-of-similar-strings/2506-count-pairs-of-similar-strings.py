class Solution:
    def similarPairs(self, words: List[str]) -> int:
        counter = 0
        Lists = []
        for item in words:
            Lists.append(list(item))
        
        for index in range(len(Lists)-1):
            pair1 = set(Lists[index])
            p1 = len(pair1)
            for index2 in range(index + 1,len(Lists)):
                pair2 = set(Lists[index2])
                p2 = len(pair2)
                mini = min(p1,p2)
                if  len(pair1.union(pair2)) == mini:
                    counter += 1
                    
        return counter
        