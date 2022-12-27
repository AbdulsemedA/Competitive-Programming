# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

def defaultdictTool(Array_A,Array_B):
    dictionA = defaultdict(list)
    set_B = set(Array_B)
    
    for index,item in enumerate(Array_A):
        dictionA[item].append(index)
        
    for item in Array_B:
        output = ''
        if item in dictionA:
            output = ' '.join([str(num+1) for num in dictionA[item]])
            print(output)
        else:
            print(-1)
                
a_size, b_size = map(int,input().split(" "))
A = []
B = []

for i in range(a_size):
    A.append(input())
    
for i in range(b_size):
    B.append(input())
    
defaultdictTool(A,B)
