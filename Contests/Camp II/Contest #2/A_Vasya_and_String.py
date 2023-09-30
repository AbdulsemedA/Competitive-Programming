n, k = map(int, input().split())
word = list(input())
maxi = 0
count = [0,0]
left = right = 0

while right < n:
    while min(count) > k and left <= right:
        count[ord(word[left]) - ord('a')] -= 1
        left += 1

    maxi = max(maxi, sum(count))
    count[ord(word[right]) - ord('a')] += 1
    right += 1

if min(count) <= k:
    maxi = max(maxi, sum(count))

print(maxi)