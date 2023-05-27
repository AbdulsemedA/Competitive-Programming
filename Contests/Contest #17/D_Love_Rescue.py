n = int(input())
valya = list(input())
tolya = list(input())
rep = {}

def finder(x):
    while x != rep[x][0]:
        x = rep[x][0] 
    return x

def union(x, y):
    fst = finder(x)
    snd = finder(y)

    if fst != snd:
        if rep[fst][1] <= rep[snd][1]:
            rep[fst][0] = snd
            rep[snd][1] += 1 + rep[fst][1]
        else:
            rep[snd][0] = fst
            rep[fst][1] += 1 + rep[snd][1]

for i in range(n):
    if valya[i] not in rep:
        rep[valya[i]] = [valya[i], 0]
    if tolya[i] not in rep:
        rep[tolya[i]] = [tolya[i], 0]
    
    union(valya[i], tolya[i])

total = 0
ans = []

for ele in rep:
    if ele != rep[ele][0]:
        ans.append([ele, rep[ele][0]])
        total += 1

print(total)
for ch, par in ans:
    print(ch, par)
