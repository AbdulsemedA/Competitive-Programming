n, d = map(int, input().split())
player = list(map(int, input().split()))
player.sort()

left = 0
right = n - 1
wins = 0
curr = 0

while left < right:
    curr = player[right]
    while left < right and curr <= d:
        curr += player[right]
        left += 1
    if curr > d:
        wins += 1
    right -= 1

if left == right:
    if player[right] > d:
        wins += 1

print(wins)