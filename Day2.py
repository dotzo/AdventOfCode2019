# https://adventofcode.com/2019/day/2

from IntCode import IntComputer
from util import filehelper as fh

program = fh.csv_to_list('day2-input.txt')

def part_1():
    computer = IntComputer(program)
    computer.run(12, 2)
    return computer.memory[0]

def part_2():
    output = 19690720
    for noun in range(100):
        for verb in range(100):
            computer = IntComputer(program)
            computer.run(noun, verb)
            if computer.memory[0] == output:
                return 100*noun + verb


if __name__ == '__main__':
    print(f"The answer to part 1 is {part_1()}") # 3790689
    print(f"The answer to part 2 is {part_2()}") # 6533
