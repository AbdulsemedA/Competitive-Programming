class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maxi = 0

        def maxLen(idx, curr):
            nonlocal maxi
            maxi = max(maxi, len(curr))
            if idx == len(arr): return

            if len(arr[idx]) == len(set(arr[idx])):
                if not curr or curr.isdisjoint(set(arr[idx])):
                    curr = curr.union(set(arr[idx]))
                    maxLen(idx + 1, curr)
                    curr = curr.difference(set(arr[idx]))

            maxLen(idx + 1, curr)
            
        maxLen(0, set())
        return maxi