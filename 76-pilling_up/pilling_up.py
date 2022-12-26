# Enter your code here. Read input from STDIN. Print output to STDOUT
def func(arr, size) -> str:
    left = 0
    right = size - 1
    pile = []

    while left != right:
        if not pile:
            if arr[left] >= arr[right]:
                pile.append(arr[left])
                left += 1
            else:
                pile.append(arr[right])
                right -= 1
        else:
            if arr[left] >= arr[right]:
                if arr[left] > pile[-1]:
                    return "No"
                else:
                    pile.append(arr[left])
                    left += 1
            else:
                if arr[right] > pile[-1]:
                    return "No"
                else:
                    pile.append(arr[right])
                    right -= 1
                    
    return "Yes"

            
t = int(input())

for i in range(t):
    size = int(input())
    arr = [int(num) for num in input().split(" ")]
    
    print(func(arr, size))
