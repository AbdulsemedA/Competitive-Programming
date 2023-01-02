def amazing(list):
    counter = 0
    maxi = list[0] 
    mini = list[0]
    list2 = [list[0]]

    for item in range(1,len(list),1):
        if list[item] > maxi:
            counter += 1
        elif list[item] < mini:
            counter += 1
            
        list2.append(list[item])
        maxi = max(list[item],maxi)
        mini = min(list[item],mini)
        
    
    print(counter)

size = int(input())
lists = list(map(int,input().split(" ")))
amazing(lists)
