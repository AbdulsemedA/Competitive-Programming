# Enter your code here. Read input from STDIN. Print output to STDOUT
def difference(english, french):
    counter = len(english.difference(french))
    
    return counter
    
english_size = int(input())
english = set(input().split(" "))

french_size = int(input())
french = set(input().split(" "))

output = difference(english,french)
print(output)
