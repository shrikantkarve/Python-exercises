"""
This is eight queens problem
https://en.wikipedia.org/wiki/Eight_queens_puzzle

This employs recursive approach to finding the solutions to
eight queen puzzle
Gives all 92 solutions
"""
import sys

solutions = []
board_size = 0


def strike_cells_queen(qcell, matrix):
    """
    This function removes the cells that can be reached by queen
    in qcell
    """
    row = qcell[0]
    column = qcell[1]
    exclusion_cells = []
    for cell in matrix:
        if cell[0] == row or cell[1] == column or \
                cell[0] + cell[1] == row + column or \
                cell[0] - row == cell[1] - column:
            exclusion_cells.append(cell)
    return [x for x in matrix if x not in exclusion_cells]


def draw_board():
    for brd in solutions:
        board = ""
        for row in range(1,board_size+1):
            for col in range(1,board_size+1):
                if [row,col] in brd:
                    board += "Q"
                else:
                    board += "-"
                board += " "
            board += "\n"
        print board


def get_queen_position(valid_cells, column, current_queen_set):
    """
    This function is a recursive function that reaches the last queen
    and records the solution when reached
    """
    if len(valid_cells) == 0:
        return
    for q in [[x, column] for x in range(1, board_size+1)
              if [x, column] in valid_cells]:

        backup_valid_cells = valid_cells
        if column == board_size:
            current_queen_set.append(q)
            solutions.append(list(current_queen_set))
            current_queen_set.pop()
        else:
            valid_cells = strike_cells_queen(q, valid_cells)
            current_queen_set.append(q)
            get_queen_position(valid_cells, column+1, current_queen_set)
            current_queen_set.pop()
            valid_cells = backup_valid_cells


def main():
    global board_size
    global solutions
    if len(sys.argv) != 2:
        print "Provide the number of columns on board as parameters"
        exit(1)

    board_size = int(sys.argv[1])
    candidate_cells = []
    for column in range(1, board_size+1):
        for row in range(1, board_size+1):
            candidate_cells.append([row, column])
    get_queen_position(candidate_cells, 1, [])
    for sol in solutions:
        print sol
    draw_board()

if __name__ == "__main__":
    main()
