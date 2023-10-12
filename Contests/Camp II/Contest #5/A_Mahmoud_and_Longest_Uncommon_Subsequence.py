a = list(input())
b = list(input())
n, m = len(a), len(b)
print(max(n, m) if a != b else -1)