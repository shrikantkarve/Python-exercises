# This is eight queens problem
# https://en.wikipedia.org/wiki/Eight_queens_puzzle

# Solution involves for loops
# provides 83 solutions out of 92 possible
# To be fixed in next version:
# 1. Try using recursion
# 2. Find all 92 solutions
# 3. Put time and memory usages, and benchmark solution

candidate_cells = []
global candidate_cells

def find_queen_position(cell_subset):
   return cell_subset[0]

def strike_cells_queen(qcell):
    row = qcell[0]
    column = qcell[1]
    global candidate_cells
    exclusion_cells = [qcell,]
    for cell in candidate_cells:
        if cell[0] == row or cell[1] == column:
            exclusion_cells.append(cell)
        if cell[0] + cell[1] == row + column:
            exclusion_cells.append(cell)
        elif cell[0] - row == cell[1] - column:
            exclusion_cells.append(cell)
    candidate_cells = [x for x in candidate_cells if x not in exclusion_cells]

for column in range(1,9):
    for row in range(1,9):
        candidate_cells.append([row,column])

for q1 in [[x,1] for x in range(1,9)]:
    q1_candidate_cells = candidate_cells
    strike_cells_queen(q1)
    for q2 in [[x,2] for x in range(1,9) if [x,2] in candidate_cells]:
        q2_candidate_cells = candidate_cells
        strike_cells_queen(q2)
        if len(candidate_cells) == 0:
            break
        for q3 in [[x,3] for x in range(1,9) if [x,3] in candidate_cells]:
            q3_candidate_cells = candidate_cells
            strike_cells_queen(q3)
            if len(candidate_cells) == 0:
                break
            for q4 in [[x,4] for x in range(1,9) if [x,4] in candidate_cells]:
                q4_candidate_cells = candidate_cells
                strike_cells_queen(q4)
                if len(candidate_cells) == 0:
                    break
                for q5 in [[x,5] for x in range(1,9) if [x,5] in candidate_cells]:
                    q5_candidate_cells = candidate_cells
                    strike_cells_queen(q5)
                    if len(candidate_cells) == 0:
                        break
                    for q6 in [[x,6] for x in range(1,9) if [x,6] in candidate_cells]:
                        q6_candidate_cells = candidate_cells
                        strike_cells_queen(q6)
                        if len(candidate_cells) == 0:
                            break
                        for q7 in [[x,7] for x in range(1,9) if [x,7] in candidate_cells]:
                            q7_candidate_cells = candidate_cells
                            strike_cells_queen(q7)
                            if len(candidate_cells) == 0:
                                break
                            for q8 in [[x,8] for x in range(1,9) if [x,8] in candidate_cells]:
                                if len(candidate_cells) == 0:
                                    break
                                print [q1, q2, q3, q4, q5, q6, q7, q8]
                            candidate_cells = q7_candidate_cells
                        candidate_cells = q6_candidate_cells
                    candidate_cells = q5_candidate_cells
                candidate_cells = q4_candidate_cells
            candidate_cells = q3_candidate_cells
        candidate_cells = q2_candidate_cells
    candidate_cells = q1_candidate_cells
