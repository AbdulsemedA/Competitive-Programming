def ehab(arr, size):
    even, odd = 0, 0
    
    for element in arr:
        if element % 2 == 0:
            even += 1
        else:
            odd += 1
        if odd and even:
            arr.sort()
            break
    
    print(*arr)
        
size = int(input())
lists = list(map(int, input().split(" ")))
ehab(lists,size)
