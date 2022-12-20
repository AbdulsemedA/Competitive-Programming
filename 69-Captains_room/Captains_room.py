# Enter your code here. Read input from STDIN. Print output to STDOUT
def captain(arr):
    hmap = {}
    for i in arr:
        hmap[i] = 1 + hmap.get(i,0)
    mini = min(hmap, key = hmap.get)
    print(mini)

size = int(input())
st = input()
arr = st.split(" ")
captain(arr)
