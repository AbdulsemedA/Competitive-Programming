def remover(lists,K):
    lists = sorted(lists, key = lambda x: x[0])
    lists = lists[K:]
    print(''.join([i[0] for i in sorted(lists, key = lambda x: x[1])]))
    
N, K = map(int,input().split())
temp = input()
myarr = [(str(temp[i]),i) for i in range(len(temp))]
remover(myarr,K)
