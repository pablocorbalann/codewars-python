# Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, 
# so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
# (More info at: http://en.wikipedia.org/wiki/Sudoku)
# Sudoku Solution Validator
# 
# Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board,
# and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.
# 
# The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.
# Examples
# 
# validSolution([
#   [5, 3, 4, 6, 7, 8, 9, 1, 2],
#   [6, 7, 2, 1, 9, 5, 3, 4, 8],
#   [1, 9, 8, 3, 4, 2, 5, 6, 7],
#   [8, 5, 9, 7, 6, 1, 4, 2, 3],
#   [4, 2, 6, 8, 5, 3, 7, 9, 1],
#   [7, 1, 3, 9, 2, 4, 8, 5, 6],
#   [9, 6, 1, 5, 3, 7, 2, 8, 4],
#   [2, 8, 7, 4, 1, 9, 6, 3, 5],
#   [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ]); // => true
# 
# validSolution([
#   [5, 3, 4, 6, 7, 8, 9, 1, 2], 
#   [6, 7, 2, 1, 9, 0, 3, 4, 8],
#   [1, 0, 0, 3, 4, 2, 5, 6, 0],
#   [8, 5, 9, 7, 6, 1, 0, 2, 0],
#   [4, 2, 6, 8, 5, 3, 7, 9, 1],
#   [7, 1, 3, 9, 2, 4, 8, 5, 6],
#   [9, 0, 1, 5, 3, 7, 2, 1, 4],
#   [2, 8, 7, 4, 1, 9, 6, 3, 5],
#   [3, 0, 0, 4, 8, 1, 1, 7, 9]
# ]); // => false

def rows(board):
    # check if the rows of the board are valid rows
    valid = 0
    for row in board:
        s = set(row)
        # conditions that have to be evaluated for every row
        set_condition = len(s) == len(board[0])
        not_empty = 0 not in s
        total_sum = sum(row) == 45
        # we evaluate those conditions for every row 
        if set_condition and not_empty and total_sum:
            valid += 1
    return True if valid == 9 else False

def columns(board):
    # checks if the columns of the board are valid columns
    inverted_board = [[] for i in range(len(board[0]))]
    for row in board:
        for counter, number in enumerate(row):
            inverted_board[counter].append(number)
    # In a sudoku a column has to be checked in the same way as a
    # row, so I have inverted the board and then I've checked it 
    # as if the columns were rows.
    return rows(inverted_board)

def boxes(board):
    # for checking if the boxes are right, we can divide the 9·9 
    # matrix in 3 smaller matrix (3·3) and then check if they 
    # are actually valid boxes.
    boxes = list()
    for i in range(0, len(board[0]), 3):
        for j in range(0, len(board[0]), 3):
            endj = j + 3
            box = board[i][j:endj] + board[i+1][j:endj] + board[i+2][j:endj]
            boxes.append(box)
    for box in boxes:
        if sum(box) != 45:
            return False
    return True
        
def valid_solution(b):
    return True if rows(b) and columns(b) and boxes(b) else False

