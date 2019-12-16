# https://adventofcode.com/2019/day/16

import numpy as np
 
def last_digit(n):
    return abs(n)%10 


#INPUT = '03081770884921959731165446850517'
INPUT = open('day16-input.txt','r').read().strip()
DIM = len(INPUT)
#print(DIM)
OFFSET = int(INPUT[:7])


def part_1():
    phase = np.array([*map(int, INPUT)])
    offset = int(INPUT[:7])
    PATTERN = np.array([0,1,0,-1])

    MATRIX = []
    for i in range(1,1+DIM):
        line = np.repeat(PATTERN, i)
        line = np.tile(line, 1 + DIM // len(line))
        line = np.roll(line, -1)[:DIM]
        MATRIX.append(line)

    MATRIX = np.row_stack(MATRIX)

    def get_phase(phase, n, mat=MATRIX):
        if n == 0:
            return phase
        else:
            return get_phase(last_digit(np.dot(MATRIX, phase)), n-1, mat=mat)

    print(f"The solution to part 1 is: {get_phase(phase, 100)[:8]}.")


## The first 7 digits of the input specify a number which maps to the 2nd half of the total
# input after replication.  As it is in the bottom half of an upper triangular matrix, 
# we can find each phase by simply rolling up the numbers from the bottom
def part_2():
    dim = DIM*10000
    phase = np.array([*map(int, INPUT[::-1])])
    phase = np.tile(phase, 10000)[:(dim-OFFSET)]
    
    for _ in range(100):
        phase = last_digit(np.cumsum(phase))

    print(f"The solution to part 2 is {phase[-1:-9:-1]}")


if __name__ == '__main__':
    part_1() #45834272
    part_2()