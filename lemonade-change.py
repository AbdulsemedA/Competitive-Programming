class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        types = defaultdict(int)
        cost = 5

        for pay in bills:
            if pay == 5:
                types[pay] += 1
                continue
            elif pay == 10:
                if types[5]:
                    types[5] -= 1
                    types[10] += 1
                else:
                    return False
            else:
                change = 0
                if types[10]:
                    types[10] -= 1
                    change += 10
                
                if change:
                    if types[5]:
                        types[5] -= 1
                    else:
                        return False
                else:
                    if types[5] > 2:
                        types[5] -= 3
                    else:
                        return False
        
        return True