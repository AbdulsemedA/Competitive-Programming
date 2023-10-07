n = int(input())
h = list(map(int, input().split()))

energy = money = 0
heights = [0] + h
n += 1

for i in range(1, n):
    energy += heights[i - 1] - heights[i]
    if energy < 0:
        money += abs(energy)
        energy = 0

print(money)