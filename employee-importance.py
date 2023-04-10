"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee = defaultdict(list)
        total = 0
        
        for ele in employees:
            employee[ele.id].extend([ele.id, ele.importance])
            employee[ele.id].extend(ele.subordinates)

        def dfs(id):
            nonlocal total
            
            curr = employee[id]
            if len(curr) == 2: return curr[1]

            temp_sum = sum(dfs(sub) for sub in employee[id][2:])
            return curr[1] + temp_sum
                    
        return dfs(id)