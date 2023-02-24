def exam(lists,points):
    column = len(lists[0])
    rows = len(lists)
    total = 0
    
    for col in range(column):
        diction = {}
        
        for row in range(rows):
            temp = lists[row][col]
            diction[temp] = 1 + diction.get(temp,0)
            
        total += max(diction.values()) * points[col]
    
    print(total)
    
N, K = map(int,input().split())
myarr = []
for _ in range(N):
    temp = input()
    myarr.append([str(i) for i in temp])
points = list(map(int,input().split()))
exam(myarr,points)
