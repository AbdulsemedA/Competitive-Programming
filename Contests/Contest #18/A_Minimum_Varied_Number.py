tc = int(input())

for _ in range(tc):
    num = int(input())
    curr = 9
    ans = []

    while num:
        if num >= curr:
            ans.append(str(curr))
            num -= curr
        curr -= 1
    
    ans = ''.join(ans[::-1])
    print(int(ans))
