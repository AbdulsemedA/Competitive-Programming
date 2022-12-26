# Enter your code here. Read input from STDIN. Print output to STDOUT
def union(english, french):
    counter = len(english.union(french))
    
    return counter
    
english_size = int(input())
english = set(input().split(" "))

french_size = int(input())
french = set(input().split(" "))

output = union(english,french)
print(output)
