V = int(input())
sor_sink = [[False, False] for _ in range(V)]

for i in range(V):
    ele = list(map(int, input().split()))

    for x in range(len(ele)):
        if ele[x] == 1:
            sor_sink[x][1] = True
            sor_sink[i][0] = True
source = []
sink = []
for i in range(len(sor_sink)):
    if sor_sink[i][1] == False:
        source.append(i+1)
    if sor_sink[i][0] == False:
        sink.append(i+1)
print(len(source), *source)
print(len(sink), *sink)