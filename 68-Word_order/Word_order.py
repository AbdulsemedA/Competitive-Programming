# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
def Wordorder(arr):
    hmap = Counter(arr)
    print(len(hmap))
    for i in hmap.values():
        print(i,end=" ")

size = int(input())
arr = []
for i in range(size):
    arr.append(input())
Wordorder(arr)
