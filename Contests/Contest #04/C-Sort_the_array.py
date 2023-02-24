n = int(input())
arr = list(map(int, input().split()))
l = 0

while l < n-1 and arr[l] <= arr[l+1]:
    l += 1
r = l
while r < n-1 and arr[r] >= arr[r+1]:
    r += 1

arr[l:r+1] = arr[l:r+1][::-1]
# print(l,r)
if arr == sorted(arr):
    print('yes')
    if l < n - 1:
        print(l+1, r+1)
    else:
        print(1, 1)

else:
    print('no')