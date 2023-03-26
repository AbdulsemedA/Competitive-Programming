def checker(a1, a2):
    if a1[0] > a2[-1]:
        return a2 + a1, 1
    return a1 + a2, 0

def checker_sort(arr):
    if len(arr) == 1:
        return arr, 0
    mid = len(arr) // 2
    left, step1 = checker_sort(arr[:mid])
    right, step2 = checker_sort(arr[mid:])
    ans, step3 = checker(left, right)
    return ans, step1 + step2 + step3

testcase = int(input())
for _ in range(testcase):
    m = int(input())
    arr = list(map(int, input().split()))
    ans, step = checker_sort(arr)
    print(step) if sorted(arr) == ans else print(-1)