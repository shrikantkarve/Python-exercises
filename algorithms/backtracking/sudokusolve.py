# This program aims to solve the sudoku puzzle in SDM format

# SDM format is a string of 81 digits. numbers 1-9 are the numbers provided
# in puzzle and 0 stands for no number.


def parse_sudoku(istr):
    # Fix: Use list comprehension to create independent rows
    sud = [[0] * 9 for _ in range(9)]

    for i in range(9):
        for j in range(9):
            st_index = i * 9 + j
            # print("st_index: {}".format(st_index))
            # print('i is {} and j is {}'.format(i,j))
            # print('char at {} is {}'.format(st_index,istr[st_index]))
            sud[i][j] = int(istr[st_index])
    return sud


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col
    return None


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


if __name__ == "__main__":
    istr = "004006079000000602056092300078061030509000406020540890007410920105000000840600100"
    board = parse_sudoku(istr)
    print("Original Board:")
    print_board(board)
    
    print("\nSolving...\n")
    solve(board)
    
    print("Solved Board:")
    print_board(board)
