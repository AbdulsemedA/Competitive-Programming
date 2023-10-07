class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        a = b = n
        total = 0
        
        costs.sort(key = lambda x: abs(x[0] - x[1]), reverse = True)
        
        for city1, city2 in costs:
            if city1 < city2:
                if a:
                    a -= 1
                    total += city1
                else:
                    total += city2
            else:
                if b:
                    b -= 1
                    total += city2
                else:
                    total += city1
        
        return total