testcase = int(input())
for _ in range(testcase):
    nums = []
    for _ in range(2):
        nums.append(list(map(int,input().split())))
    # print(nums)
    if nums[0][0] < nums[0][1] and nums[1][0] < nums[1][1]:
        if nums[1][0] > nums[0][0] and nums[1][1] > nums[0][1]:
            print("YES")
        elif nums[1][0] < nums[0][0] and nums[1][1] < nums[0][1]:
            print("YES")
        else:
            print("NO")
            
    elif nums[0][0] > nums[0][1] and nums[1][0] > nums[1][1]:
        if nums[1][0] > nums[0][0] and nums[1][1] > nums[0][1]:
            print("YES")
        elif nums[1][0] < nums[0][0] and nums[1][1] < nums[0][1]:
            print("YES")
        else:
            print("NO")
    
    else:
        print("NO")