# This is program to create a sequence of number following
# collatz conjecture

# If a number is odd, multiply it by 3 and add 1
# If number if even, divide by 2

import argparse
import pprint
import sys

seq_len = {}
seq_dict = {}
highest = {}

def get_seq(num):

    global seq_dict
    start_num = num
    sequence = [num]
    #sequence.append(num)
    #print(num)
    while(True):
        if num == 1:
            #print(",".join(map(str, sequence)))
            break
        elif num%2 == 0:
            num = num//2
            #sequence.append(num)
        else:
            num = 3 * num + 1
            #sequence.append(num)
        if num <= start_num:
            sequence.extend(seq_dict[num])
            break
        else:
            sequence.append(num)
    return sequence

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--max_num", required=True, type=int,
                        help="Provide the max number you want to calculate\
                             collatx sequence")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()
    print(args)

    high = 1
    for i in range(1,args.max_num+1):
        seq_dict[i] = get_seq(i)
        seq_len[i] = len(seq_dict[i]) 
        if seq_len[i] >= high:
            high = seq_len[i]
        highest[i] = high 
        if args.verbose:
            print("sequence for ",i,":",",".join(map(str,seq_dict[i])))
    if args.verbose:
        for i in sorted(seq_len.keys()):
            print("{0:6} : {1:4} : {2:4}".format(i, seq_len[i], highest[i]))
main()
