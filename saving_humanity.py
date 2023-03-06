tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split(" "))
    nums = list(map(int, input()))
    
    for _ in range(min(m, n)):
        i = 0
        already = set()
        while i < n:
            if nums[i] == 0:
                if i > 0 and i < n-1:
                    if i-1 not in already:
                        if nums[i-1] + nums[i+1] == 1:
                            nums[i] = 1
                            already.add(i)
                    else:
                        if nums[i+1] == 1:
                            nums[i] = 1
                            already.add(i)
                        # print(nums[i])
                elif i == 0:
                    if nums[i+1] == 1:
                        nums[i] = 1
                        already.add(i)
                        # print(nums[i])
                else:
                    if i-1 not in already:
                        if nums[i-1] == 1:
                            nums[i] = 1
                            already.add(i)
                        # print(nums[i])
            i += 1
    
    print(''.join([str(a) for a in nums]))
