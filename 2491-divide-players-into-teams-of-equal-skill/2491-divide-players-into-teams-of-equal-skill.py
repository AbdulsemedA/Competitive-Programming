class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        teams = set()
        chemistry = 0
        left, right = 0, n - 1
        
        while left < right:
            teams.add(skill[left] + skill[right])
            chemistry += skill[left] * skill[right]
            right -= 1
            left += 1
        
        if len(teams) == 1:
            return chemistry
        return -1
        
        