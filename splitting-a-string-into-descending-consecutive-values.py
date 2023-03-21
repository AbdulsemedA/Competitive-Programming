class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)

        def helper(s, prev_num, count):
            if not s and count > 1:
                return True
            for i in range(1, n + 1):
                num = int(s[:i])
                if num < prev_num and (prev_num - num) == 1:
                    if helper(s[i:], num, count+1):
                        return True
            return False
    
        
        for i in range(1, n):
            num1 = int(s[:i])
            if num1 == 0:
                continue
            if helper(s[i:], num1, 1):
                return True
        return False