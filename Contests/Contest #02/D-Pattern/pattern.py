def pattern(word):
    row = len(word)
    col = len(word[0])
    result = ""
    
    for i in range(col):
        sets = {}
        sequence  = ""
        
        for j in range(row):
            if word[j][i] == "?":
                continue
            else:
                sets[word[j][i]] = 1 + sets.get(word[j][i],0)
                sequence += word[j][i]
                
        if len(sets) > 1:
            result += "?"
        else:
            if len(sequence) > 0:
                result += sequence[0]
            else:
                result += "a"
    
    print(result)
            
            
            
    
size = int(input())
words = []

for _ in range(size):
    words.append(input())
    
pattern(words)
