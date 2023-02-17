testcase = int(input())
for _ in range(testcase):
    n, m, k = map(int, input().split())
    a = list(input())
    b = list(input())
    a.sort()
    b.sort()
    c = []

    a_count = 0
    b_count = 0

    i = j = 0

    while i < n and j < m:
        if a[i] <= b[j]:
            if a_count < k:
                c.append(a[i])
                i += 1
                a_count += 1
                b_count = 0
            else:
                c.append(b[j])
                j += 1
                b_count += 1
                a_count = 0
        else:
            if b_count < k:
                c.append(b[j])
                j += 1
                b_count += 1
                a_count = 0
            else:
                c.append(a[i])
                i += 1
                a_count += 1
                b_count = 0
    
    print(''.join(c))
