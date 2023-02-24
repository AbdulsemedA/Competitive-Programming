def pronounce(word):
    print(word[:2],end="... ")
    print(word,end="")
    print("?")

size = int(input())
for _ in range(size):
    pronounce(input())
