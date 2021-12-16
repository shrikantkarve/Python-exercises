# This program aims to solve the sudoku puzzle in SDM format

# SDM format is a string of 81 digits. numbers 1-9 are the numbers provided
# in puzzle and 0 stands for no number.

istr = "004006079000000602056092300078061030509000406020540890007410920105000000840600100"

sud = [[0] * 9] * 9

for i in range(9):
    for j in range(9):
        st_index = i*9 + j
        print("st_index: {}".format(st_index))
        print('i is {} and j is {}'.format(i,j))
        print('char at {} is {}'.format(st_index,istr[st_index]))
        sud[i][j] = istr[st_index]

print(sud)
