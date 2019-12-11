# https://adventofcode.com/2019/day/9

from IntcodeComputer import Machine

#INPUT = open('day9-input.txt','r').read()
INPUT = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'
INPUT = list(map(int, INPUT.split(',')))

program = Machine(INPUT)
out = ''
while program.is_running:
    out += str(program.run())
    out += ','
print(out)