class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtrack(num, i, prev1, prev2):
            if i == len(num):
                return True

            for j in range(i+1, len(num)+1):
                if j > i+1 and num[i] == '0':
                    break
                cur = int(num[i:j])
                
                if cur == prev1 + prev2:
                    if backtrack(num, j, prev2, cur):
                        return True
                elif cur > prev1 + prev2:
                    break

            return False
    
        for i in range(1, len(num)):
            if i > 1 and num[0] == '0':
                break
            num1 = int(num[:i])
            for j in range(i+1, len(num)):
                if j > i+1 and num[i] == '0':
                    break
                num2 = int(num[i:j])
                if backtrack(num, j, num1, num2):
                    return True
        return False
        if len(num) > 2:
            return backrack(num, 0, num[0],num[1])
        return False