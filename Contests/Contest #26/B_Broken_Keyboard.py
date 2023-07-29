# broken keyboard

testcases = int(input())

for i in range(testcases):
    text = input()
    defects = set()
    pure = set()

    if len(text) == 1:
        print(text)
    
    else:
        curr = text[0]
        count = 1
        for j in range(1, len(text)):
            if text[j] == curr:
                count += 1
            else:
                if count % 2 == 0 and curr not in pure:
                    defects.add(curr)
                if count % 2:
                    defects.discard(curr)
                    pure.add(curr)
                curr = text[j]
                count = 1
        if count % 2 == 0 and curr not in pure:
            defects.add(curr)
        if count % 2:
            defects.discard(curr)
            pure.add(curr)
    
        print(''.join(sorted(pure)))


