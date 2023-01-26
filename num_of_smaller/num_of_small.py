n, m = map(int,input().split(' '))
arr1 = list(map(int, input().split(' ')))
arr2 = list(map(int, input().split(' ')))
curr = 0

for val in arr2:
    while curr < n and arr1[curr] < val:
        curr += 1
    print(curr,end=" ")
