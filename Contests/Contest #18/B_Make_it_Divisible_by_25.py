tc = int(input())

for _ in range(tc):
    str = input()
    min_steps = float('inf')
    
    for ending in ['00', '25', '50', '75']:
        steps = 0
        idx = len(str) - 1
        ending_idx = len(ending) - 1
        
        while idx >= 0 and ending_idx >= 0:
            if str[idx] == ending[ending_idx]:
                ending_idx -= 1
            steps += 1
            idx -= 1
            
        if ending_idx == -1:
            min_steps = min(min_steps, steps - 2)
            
           
    print(min_steps)
