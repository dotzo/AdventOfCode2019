# https://adventofcode.com/2019/day/2

from IntCode import IntComputer

program = list(map(int,open('day2-input.txt','r').read().split(',')))

def part_1():
    computer = IntComputer(program)
    computer.run(12, 2)
    print(computer.memory[0])

def part_2():
    output = 19690720
    for noun in range(100):
        for verb in range(100):
            computer = IntComputer(program)
            computer.run(noun, verb)
            if computer.memory[0] == output:
                return 100*noun + verb

part_1()
print(part_2())
