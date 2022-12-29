if __name__ == '__main__':
    n = int(input())
    _lists = tuple(map(int, input().split()))
    
    print(hash(_lists))
