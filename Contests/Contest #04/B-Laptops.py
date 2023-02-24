n = int(input())
priceList = []
qualityList = []
for i in range(n):
    p, q = [int(x) for x in input().split()]
    priceList.append(p)
    qualityList.append(q)

priceList, qualityList = zip(*sorted(zip(priceList, qualityList)))

check = False
for i in range(n - 1):
    if priceList[i] < priceList[i+1] and qualityList[i] > qualityList[i+1]:
        check = True
 
if check:
    print("Happy Alex")
else:
    print("Poor Alex")