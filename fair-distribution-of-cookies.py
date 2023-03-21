class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        cookies.sort(reverse = True)
        children = [0] * k
        mini = float('inf')

        def allocate(idx):
            nonlocal mini, children
            if idx == n:
                mini = min(mini, max(children))
                return
            if mini <= max(children):
                return
            
            for i in range(k):
                children[i] += cookies[idx]
                allocate(idx + 1)
                children[i] -= cookies[idx]
            
        allocate(0)
        return mini