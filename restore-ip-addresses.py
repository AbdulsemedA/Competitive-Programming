class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = set()
        
        def ipValidate(s, arr, count):
            if not s or count > 4:
                if count == 4: result.add(".".join(arr))
                return
            
            for i in range(1, 4):
                curr = s[:i]
                if curr.startswith("0") and len(curr) > 1: continue
                num1 = int(s[:i])
                if num1 > -1 and num1 < 256:
                    ipValidate(s[i:], arr + [str(num1)], count + 1)

        ipValidate(s, [], 0)
        return result