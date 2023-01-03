def planet(lists,K):
    result = 0
    dictionary = {}
        
    for item in lists:
        dictionary[item] = 1 + dictionary.get(item,0)
        
    for item in dictionary:
        if dictionary[item] >= K:
            result += K
        else:
            result += dictionary[item]
    
    print(result)
    
N = int(input())

for _ in range(N):
    size, K = map(int,input().split())
    lists = list(map(int,input().split()))
    planet(lists,K)
