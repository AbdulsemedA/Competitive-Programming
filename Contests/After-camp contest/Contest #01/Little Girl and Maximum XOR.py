l, r = map(int, input().split())
print(int("1" * (len(bin(l ^ r)) - 2) , 2)) if l ^ r != 0 else print(0)