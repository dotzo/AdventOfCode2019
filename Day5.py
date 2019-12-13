# https://adventofcode.com/2019/day/5

from util import filehelper as fh
from IntCode import IntComputer

program = fh.csv_to_list('day5-input.txt')

def part_1():
    computer = IntComputer(program, inputs=[1])
    return computer.run()

def part_2():
    computer = IntComputer(program, inputs=[5])
    return computer.run()

if __name__ == '__main__':
    print(f"The answer to part 1 is {part_1()}") # 9006673
    print(f"The answer to part 2 is {part_2()}") # 3629692