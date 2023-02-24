def count_indices(n, k, tests):
    count = 0
    run = 0
    j = 1
    
    while j < n:
        if (2 * tests[j]) > tests[j-1]:
            run += 1
        else:
            if run >= k:
                count += run - k + 1
            run = 0
        j += 1
    if run == n - 1:
        print(n - k)
    else: 
        if run >= k:
            count += run - k + 1
        print(count)

ts = int(input())
for item in range(ts):
    a, b = map(int,input().split(' '))
    num = list(map(int, input().split(' ')))
    count_indices(a, b, num)