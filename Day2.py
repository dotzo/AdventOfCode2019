# https://adventofcode.com/2019/day/2

STATE = list(map(int,open('day2-input.txt','r').read().split(',')))
STATE[1] = 12
STATE[2] = 2
COUNTER = 0
def execute(state):
    global COUNTER
    op = state[COUNTER:COUNTER+4]
    COUNTER += 4
    if len(op) == 4:
        opcode, addr1, addr2, ra = op
    else:
        opcode = op[0]

    if opcode == 99:
        pass
    elif opcode == 1:
        STATE[ra] = state[addr1] + state[addr2]
        execute(STATE)
    elif opcode == 2:
        STATE[ra] = state[addr1] * state[addr2]
        execute(STATE)

execute(STATE)
print(STATE[0])