def comparator(lists):
    compared = sorted(lists, key = lambda x: (x[-1], x.count("X")))
    if lists[0] == lists[1]:
        print("=")
    else:
        if lists[0][-1] != lists[1][-1]:
            if lists[0] != compared[0]:
                print("<")
            else:
                print(">")
        else:
            if lists[0][-1] == "S":
                if lists[0] != compared[0]:
                    print("<")
                else:
                    print(">")
            else:
                if lists[0] != compared[0]:
                    print(">")
                else:
                    print("<")

N = int(input())
for _ in range(N):
    mylist = input().split(" ")
    comparator(mylist)
