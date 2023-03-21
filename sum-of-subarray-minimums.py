class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        stack = []
        res = 0

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                j = stack.pop()
                print(j)
                k = stack[-1] if stack else -1
                print("J: ",j)
                res += arr[j] * (i - j) * (j - k)
                print("res: ",res)
                res %= MOD
                

            stack.append(i)

        while stack:
            j = stack.pop()
            k = stack[-1] if stack else -1
            res += arr[j] * (n - j) * (j - k)
            res %= MOD
            print(res)

        return res