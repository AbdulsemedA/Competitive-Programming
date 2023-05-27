n, d = map(int, input().split())
rep = {i: [i, 0] for i in range(1, n + 1)}

def finder(x):
    while x != rep[x][0]:
        x = rep[x][0] 
    return x

def union(x, y):
    fst = finder(x)
    snd = finder(y)

    if fst != snd:
        if rep[fst][1] < rep[snd][1]:
            rep[fst][0] = snd
            rep[snd][1] += 1 + rep[fst][1]
            return rep[snd][1]
        else:
            rep[snd][0] = fst
            rep[fst][1] += 1 + rep[snd][1]
            return rep[fst][1]
    
    return rep[fst][1]

# print(rep)
maxi = 0

for _ in range(d):
    src, des = map(int, input().split())
    ele = union(src, des)

    if ele > maxi:
        maxi = ele
    
    print(maxi)
