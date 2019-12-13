# https://adventofcode.com/2019/day/7

from util import filehelper as fh
from IntCode import IntComputer
from itertools import permutations

program = fh.csv_to_list('day7-input.txt')

def amplifyer(phase):
    computers = []
    for p in phase:
        computers.append(IntComputer(program, inputs=[p], wait_for_input=True, wait_after_output=True))
        computers[-1].run()

    in_out = 0
    max_output = 0
    while not computers[0].finished:
        for comp in computers:
            comp.inputs = [in_out]
            in_out = comp.run()

    max_output = max(max_output, in_out)

    return max_output


def part_1():
    return max(map(amplifyer, permutations([0,1,2,3,4])))

def part_2():
    return max(map(amplifyer, permutations([5,6,7,8,9])))

if __name__ == '__main__':
    print(f"The answer to part 1 is {part_1()}") # 17440
    print(f"The answer to part 2 is {part_2()}") # 27561242