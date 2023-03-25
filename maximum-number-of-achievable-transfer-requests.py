class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        employee = [0] * n
        max_achieve = 0

        def transfer(idx, size, employee, req):
            nonlocal max_achieve
            if len(set(employee)) == 1 and not employee[0]: 
                max_achieve = max(max_achieve, size)
            if idx == len(req): 
                return

            frm, to = requests[idx]
            emp = employee[:]
            emp[frm] -= 1
            emp[to] += 1

            transfer(idx + 1, size + 1, emp, req)
            transfer(idx + 1, size, employee, req)
        
        transfer(0, 0, employee, requests)
        return max_achieve