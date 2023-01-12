def xsum(x) -> int:
    forward = {}
    backward = {}
    maximum = 0

    for row in range(len(x)):
        for col in range(len(x[0])):
            forward[row+col] = x[row][col] + forward.get(row+col,0)
            backward[row-col] = x[row][col] + backward.get(row-col,0)
    
    for row in range(len(x)):
        for col in range(len(x[0])):
            maximum = max(maximum, forward[row+col] + backward[row-col] - x[row][col])
            
    return maximum

size = int(input())

for _ in range(size):
    row, col = map(int,input().split())
    Lists = []
    
    for _ in range(row):
        Lists.append(list(map(int,input().split())))
        
    result = xsum(Lists)
    print(result)
