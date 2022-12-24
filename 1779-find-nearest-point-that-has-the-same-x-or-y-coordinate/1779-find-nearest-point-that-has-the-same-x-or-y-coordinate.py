class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dictionary = {}
        size = len(points)
        Manhattan_distance = 0
        
        for index in range(size):
            if points[index][0] == x or points[index][1] == y:
                if index not in dictionary:
                    Manhattan_distance = abs(points[index][0] - x) + abs(points[index][1] - y)
                    dictionary[index] = Manhattan_distance
        
        if len(dictionary) == 0:
            return -1
        return min(dictionary, key = dictionary.get)
        