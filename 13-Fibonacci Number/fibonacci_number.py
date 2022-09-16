class Solution:
    def fib(self, n: int) -> int:
        arr = []
        arr.append(0)
        arr.append(1)
        for i in range(n):
            if i >= 2:
                arr.append(arr[i-1] + arr[i-2])
        if n >= 2:
            result = arr[n-1] + arr[n-2]
        else:
            result = arr[n]
        return result
