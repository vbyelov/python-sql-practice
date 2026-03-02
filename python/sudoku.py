board = []

for i in range(9):
    line = input(f"Enter row {i+1}: ")

    if len(line) != 9:
        print("No")
        exit()

    row = []

    for ch in line:
        if not ch.isdigit():
            print("No")
            exit()
        row.append(int(ch))

    board.append(row)

sample = {1,2,3,4,5,6,7,8,9}

for row in board:
    if set(row) != sample:
        print("No")
        exit()

for col in range(9):
    column = []
    for row in range(9):
        column.append(board[row][col])

    if set(column) != sample:
        print("No")
        exit()

for start_row in range(0, 9, 3):
    for start_col in range(0, 9, 3):

        block = []

        for i in range(3):
            for j in range(3):
                block.append(board[start_row + i][start_col + j])

        if set(block) != sample:
            print("No")
            exit()