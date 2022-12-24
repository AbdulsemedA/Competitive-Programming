class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary = salary[1:len(salary)-1]
        return sum(salary) / len(salary)