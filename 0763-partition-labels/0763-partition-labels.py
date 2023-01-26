class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end_indexes = {}
        result = []
        size, left = len(s), 0,
        sums = 0
        
        for idx, val in enumerate(s):
            end_indexes[val] = idx
        
        right = end_indexes[s[left]]
        
        while left < size and right < size:
            while left <= right:
                if end_indexes[s[left]] > right:
                    right = end_indexes[s[left]]
                left += 1
            result.append(left - sums)
            sums += result[-1]
            if left == size:
                right = end_indexes[s[left-1]]
            else:
                right = end_indexes[s[left]]
        
        return result
            
                
        
            
        
        
        