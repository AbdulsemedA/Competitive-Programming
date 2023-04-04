tc = int(input())
for _ in range(tc):
    num = int(input())
    
    if num & 1:
        num >>= 1
        if num > 0:
            print(1)
        else:
            print(3)
    else:
        ans = ""
        if bin(num).count("1") > 1:
            while num & 1 == 0:
                ans = "0" + ans
                num >>= 1
            ans = "1" + ans
            print(int(ans, 2))

        else:
            num >>= 1
            while num & 1 == 0:
                ans = "0" + ans
                num >>= 1
        
            print(int("1" + ans + "1", 2))