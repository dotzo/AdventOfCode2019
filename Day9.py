# https://adventofcode.com/2019/day/9

from IntcodeComputer import Machine

INPUT = open('day9-input.txt','r').read()
INPUT = list(map(int, INPUT.split(',')))

program = Machine(INPUT)
print(program.run(2))