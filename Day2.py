# https://adventofcode.com/2019/day/2

BASE_STATE = list(map(int,open('day2-input.txt','r').read().split(',')))
OOB = len(BASE_STATE)
def program(code, *args, return_address=0):
    memory = list(code)    
    for (a,v) in args:
        memory[a] = v
    COUNTER = 0
    
    def execute(count):
        opcode = memory[count]
        if opcode == 1:
            _, a1, a2, ra = memory[count:count+4]
            memory[ra] = memory[a1] + memory[a2]
            return count+4
        elif opcode == 2:
            _, a1, a2, ra = memory[count:count+4]
            memory[ra] = memory[a1] * memory[a2]
            return count+4
        elif opcode == 99:
            return -1
        else: return -2
    
    while COUNTER < OOB:
        r = execute(COUNTER)
        if r == -1:
            return memory[return_address]
        else:
            COUNTER = r
    else:
        return -1

for noun in range(0,100):
    for verb in range(0,100):
        if program(BASE_STATE, (1,noun), (2,verb)) == 19690720:
            print(noun, verb, 100*noun + verb)
            break