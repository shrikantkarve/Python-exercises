# This is solution to towers of hanoi puzzle
# The objective of the puzzle is to move the entire stack to another rod,
# obeying the following simple rules:

# 1. Only one disk can be moved at a time.
# 2. Each move consists of taking the upper disk from one of the stacks and
# placing it on top of another stack or on an empty rod.
# 3. No disk may be placed on top of a smaller disk.

src = list(range(1, 6))
tgt = []
standby = []


# Want to move all elements in same order to B
def move_elem(A, B, C, level):
    if level == 1:
        B.append(A.pop())
    else:
        move_elem(A, C, B, level-1)
        move_elem(A, B, C, 1)
        move_elem(C, B, A, level-1)


def print_pegs():
    print(src)
    print(tgt)
    print(standby)


print("Before movement:")
print_pegs()
move_elem(src, tgt, standby, len(src))
print("After movement:")
print_pegs()
