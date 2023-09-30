n = int(input())
A = list(map(int, input().split()))
B = list(map(int,input().split()))

Upper = [A[-1],0]
Lower = [B[-1],0]

for index in range(n-1,0,-1):
    curr1, curr2 = Upper, Lower
    Lower = [max(curr1)+B[index-1], max(curr2)]
    Upper = [max(curr2) + A[index-1], max(curr1)]

print(max(max(Upper,Lower)))