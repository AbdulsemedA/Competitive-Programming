class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        
        common = ""
        current = 0
        size_of_first_element = len(strs[0])
        
        if size_of_first_element > 0:
            minimum = min(len(strs[0]),len(strs[-1]))
            
            while current < minimum and strs[0][current] == strs[-1][current]:
                common += strs[0][current]
                current += 1

        return common
            
        
        