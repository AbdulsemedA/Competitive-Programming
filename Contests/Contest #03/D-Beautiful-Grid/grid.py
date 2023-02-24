def beauty_grid(grid):
    counter = 0
    left, right = 0, len(grid) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right

            C1 = grid[top][left + i]
            C2 = grid[bottom - i][left]
            C3 = grid[bottom][right - i]
            C4 = grid[top + i][right]

            P1 = (C1 + C2 + C3 + C4)
            if P1 < 2:
                counter += P1
            else:
                counter += 4 - P1
        left += 1
        right -= 1
    print(counter)

inputs = int(input())
for _ in range(inputs):
    size = int(input())
    grids = []
    for _ in range(size):
        st = input()
        grids.append([int(ch) for ch in st])
    beauty_grid(grids)
