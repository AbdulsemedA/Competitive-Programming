given = list(map(int, input()))
answer = list(map(int, input()))
given.sort()

for i in range(len(given)):
    if given[i]:
        given[i], given[0] = given[0], given[i]
        break

if given == answer:
    print("OK")
else:
    print("WRONG_ANSWER")