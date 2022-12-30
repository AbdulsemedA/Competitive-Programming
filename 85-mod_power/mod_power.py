# Enter your code here. Read input from STDIN. Print output to STDOUT
def power(a,b,m):
    powers = pow(a,b)
    print(powers)
    
    result = powers % m
    print(result)
    
a = int(input())
b = int(input())
m = int(input())
power(a,b,m)
