def chess(board):
    m = len(board)
    n = len(board[0])

    for i in range(m):
        for j in range(n):
            if i + 2 < m and j + 2 < n and board[i][j] == '#':
                if board[i][j+2] == board[i+2][j] == board[i+2][j+2] == '#':
                    print(f'{i+2} {j+2}')
                    break


inputs = int(input())
for _ in range(inputs):
    dump = input()
    boards = []
    for _ in range(8):
        strings = input()
        boards.append([ch for ch in strings])
    chess(boards)
