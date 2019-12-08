# https://adventofcode.com/2019/day/7

from IntcodeComputer import Machine
from itertools import permutations

with open('day7-input.txt','r') as f:
    contents = [int(i.strip()) for i in f.read().split(',')]

max_output = 0

for phases in permutations([5,6,7,8,9]):
    #print("Phase: ", phases)
    machines = []
    for phase in phases:
        machines.append(Machine(contents))
        machines[-1].phase_setup(phase)
    
    
    in_out = 0

    while machines[0].is_running:
        for machine in machines:
            in_out = machine.run(in_out)
    max_output = max(max_output, in_out)

print(f"max output: {max_output}")
