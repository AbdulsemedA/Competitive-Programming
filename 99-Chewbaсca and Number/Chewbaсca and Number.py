def minimum(lists):
    for item in range(len(lists)):
        if item == 0:
            if lists[item] != 9 and lists[item] > 4:
                lists[item] = 9 - lists[item]
        else:
            if lists[item] > 4:
                lists[item] = 9 - lists[item]
    
    if lists[0] == 0:
        lists.pop(0)
    print(''.join([str(item) for item in lists]))

num = input()
myarr = [int(i) for i in num]
minimum(myarr)
