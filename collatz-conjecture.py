# This is program to create a sequence of number following
# collatz conjecture

# If a number is odd, multiply it by 3 and add 1
# If number if even, divide by 2

import sys
sequence = []

if len(sys.argv) != 2:
    print("Provide a number to print sequence of")
    exit(-1)
num = int(sys.argv[1])
sequence.append(num)
#print(num)
while(True):
    if num == 1:
        print(",".join(map(str, sequence)))
        exit(0)
    if num%2 == 0:
        num = num//2
        sequence.append(num)
    else:
        num = 3 * num + 1
        sequence.append(num)

