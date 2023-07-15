s = input()
if "AB" in s:
    index_ab = s.index("AB")
    if "BA" in s[index_ab + 2:]:
        print("YES")
        exit()

if "BA" in s:
    index_ba = s.index("BA")
    
    if "AB" in s[index_ba + 2:]:
        print("YES")
        exit()

print("NO")