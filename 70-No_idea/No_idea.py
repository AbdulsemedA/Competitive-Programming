# Enter your code here. Read input from STDIN. Print output to STDOUT
def Hapiness(L,A,B):
    hapiness = 0
    for i in L:
        if i in A:
            hapiness += 1
        if i in B:
            hapiness -= 1
    print(hapiness)

n = input().split(" ")
L = input().split(" ")
A = set(input().split(" "))
B = set(input().split(" "))
Hapiness(L, A, B)
