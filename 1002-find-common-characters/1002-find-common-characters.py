import collections
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        Hmap = defaultdict(list)
        answer = []
        
        for item in range(len(words)):
            current = {}
            
            for ch in words[item]:
                current[ch] = 1 + current.get(ch,0)
                
            for item in current:
                Hmap[item].append(current[item]) 
        
        for item in Hmap:
            if len(Hmap[item]) == len(words):
                for _ in range(min(Hmap[item])):
                    answer.append(item)
                               
        return answer
                
                
        