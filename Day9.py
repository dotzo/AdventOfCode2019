# https://adventofcode.com/2019/day/9

from IntcodeComputer import Machine
from util import filehelper as fh
from IntCode import IntComputer


program = fh.csv_to_list('day9-input.txt')

def part(n):
    computer = IntComputer(program, inputs=[n])
    return computer.run()


if __name__ == '__main__':
    print(f"The answer to part 1 is {part(1)}") # 2316632620
    print(f"The answer to part 2 is {part(2)}") # 78869