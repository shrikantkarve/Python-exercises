# Given a 2D matrix as below:
# [1, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 0]

# Find out any cell that has all surounding zeros. That is an island.
# Diagonal cells also must be considered

grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 1, 0, 1],
]

def surr_paths(cell):
    global grid
    paths = []
    for x in range(-1,2,1):
        for y in range(-1,2,1):
            if (x == 0 and y == 0):
                pass
            paths.append([cell[0]+x,cell[1]+y],)
    #print("paths: ", paths)
    return paths

def is_valid_cell(cell):
    # return True is cell is on board and doesn't cross the bounds
    if cell[0] < 0 or cell[0] >= len(grid[0]) or cell[1] < 0 or cell[1] >= len(grid):
        #print("Invalid cell: ", cell)
        return False 
    else:
        return True


def no_of_islands(grid):
    num_islands = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            is_island = True
            for path in surr_paths([row,col]):
                #is_island = True
                if not is_valid_cell(path):
                    continue
                elif grid[path[0]][path[1]] == 1:
                    is_island = False
            if is_island:
                #print("Island identified is : ", [row, col])
                num_islands+=1


    return num_islands

if __name__ == '__main__':
    print("Number of islands identified in the grid are %i" % no_of_islands(grid))