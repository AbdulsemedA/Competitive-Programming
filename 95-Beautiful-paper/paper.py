def paper(lists) -> str:
    maxi1 = max(lists[0])
    maxi2 = max(lists[1])
    lists[0].remove(maxi1)
    lists[1].remove(maxi2)

    if maxi1 == maxi2:
        if lists[0][0] + lists[1][0] == maxi1:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

size = int(input())
for _ in range(size):
    mylist = []
    for _ in range(2):
        mylist.append(list(map(int,input().split())))
    paper(mylist)
