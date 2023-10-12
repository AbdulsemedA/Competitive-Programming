S1 = input()
S2 = input()
differ = 0
i = j = 0
stat = True
idx = len(S1) - 1

while i < len(S1) and j < len(S2):
    if S1[i] != S2[j]:
        differ += 1
        idx = i
        i += 1
        
        if differ > 1:
            stat = False
            break
    else:
        i += 1
        j += 1

ans = [idx + 1]

if stat:
    while idx:
        if S1[idx - 1] == S1[idx]:
            ans.append(idx)
            idx -= 1
            continue
        break

    print(len(ans))
    print(*ans[::-1])

else:
    print(0)

