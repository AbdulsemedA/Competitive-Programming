from collections import Counter

def cross(lists, n, m) -> None:
    colMap = [Counter(cols) for cols in zip(*lists)]
    rowMap = [Counter(rows) for rows in lists]

    for row in range(n):
        for col in range(m):
            if rowMap[row][crossword[row][col]] == 1:
                if colMap[col][crossword[row][col]] == 1:
                    print(crossword[row][col], end="")
                    
n, m = map(int, input().split())
crossword = []
for _ in range(n):
    crossword.append(list(input()))
cross(crossword, n, m)
