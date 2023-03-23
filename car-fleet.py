class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 1
        size = len(position)
        cars = [(position[i], speed[i]) for i in range(size)]
        cars = sorted(cars, key = lambda x: x[0],reverse=True)
        l = 0

        for i in range(1, size):
            cur = (target - cars[l][0]) / cars[l][1]
            nxt = (target - cars[i][0]) / cars[i][1]

            if nxt > cur:
                l = i
                fleets += 1
                
        return fleets