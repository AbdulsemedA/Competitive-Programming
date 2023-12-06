class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr = idx = 0
        if sum(gas) < sum(cost): return -1

        for i in range(len(gas)):
            curr += gas[i] - cost[i]
            if curr < 0:
                curr = 0
                idx = i + 1
        
        return idx