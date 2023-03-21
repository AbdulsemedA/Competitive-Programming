n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

answer = (m // (k + 1)) * (k*nums[-1] + nums[-2])
answer += (m % (k + 1)) * nums[-1]
print(answer)