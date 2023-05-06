import heapq

tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    board = list(map(int, input().split()))
    oper = list(map(int, input().split()))
    
    heapq.heapify(board)
    for i in oper:
        heapq.heapreplace(board, i)
    
    print(sum(board))
