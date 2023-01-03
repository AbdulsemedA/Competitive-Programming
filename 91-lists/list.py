if __name__ == '__main__':
    N = int(input())
    array = []
    
    for _ in range(N):
        lists = input().split(" ")
        if lists[0] == "insert":
            array.insert(int(lists[1]),int(lists[2]))
        elif lists[0] == "print":
            print(array)
        elif lists[0] == "remove":
            array.remove(int(lists[1]))
        elif lists[0] == "append":
            array.append(int(lists[1]))
        elif lists[0] == "sort":
            array.sort()
        elif lists[0] == "pop":    
            array.pop()
        elif lists[0] == "reverse":
            array.reverse()
