sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def print_sudoku_board(board):
    # iterate through the rows and add line breaks at every third row
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        # iterate through the columns and add line breaks at every third column
        for j in range(len(board[0])):
            if j % 3 == 0 and j!= 0:
                print("| ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def search_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j
    return None


def check_sudoku_board(board, number, position):
    # check the row for repeated number
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False
    # check the column for repeated number
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    box_row = (position[0] // 3) * 3
    box_col = (position[1] // 3) * 3

    # check the box for repeated number
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == number and (i, j) != position:
                return False

    return True


def solve_sudoku_board(board):
    empty = search_empty(board)
    # base case for the recursive col - if the board is not empty, it is solved
    if not empty:
        return True
    else:
        row, col = empty
    # iterate through the board adding numbers and checking validity
    for i in range(1, 10):
        if check_sudoku_board(board, i, (row, col)):
            board[row][col] = i

            if solve_sudoku_board(board):
                return True
            else:
                board[row][col] = 0

    return False


print("----Unsolved Board----")
print_sudoku_board(sudoku_board)
solve_sudoku_board(sudoku_board)
print("-----Solved Board-----")
print_sudoku_board(sudoku_board)
