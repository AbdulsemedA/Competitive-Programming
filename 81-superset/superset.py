# Enter your code here. Read input from STDIN. Print output to STDOUT
def superset(Set,List_sets) -> bool:
    for item in List_sets:
        if not Set.issuperset(item) or item == Set:
            return False
    
    return True

Set_A = set(input().split(" "))
size_ofSet = int(input())
sets = []

for _ in range(size_ofSet):
    sets.append(set(input().split(" ")))

print(superset(Set_A,sets))


    
