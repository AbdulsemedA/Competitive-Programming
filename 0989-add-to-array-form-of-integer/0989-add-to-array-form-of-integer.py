class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        Num = 0
        for i in num:
            Num = 10 * Num + i
        
        return list(map(int, str(Num + k)))
    
        