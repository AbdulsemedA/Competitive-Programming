class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = [0] * 101

        for birth, death in logs:
            population[birth - 1950] += 1
            population[death - 1950] -= 1
        
        for i in range(1, len(population)):
            population[i] += population[i-1]
        
        ans = population.index(max(population))
        return ans + 1950