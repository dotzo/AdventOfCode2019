# https://adventofcode.com/2019/day/11

from IntcodeComputer import Machine
from functools import reduce

INPUT = open('day11-input.txt','r').read()
INPUT = list(map(int, INPUT.split(',')))
LOG = open('log.txt','w')

robot = Machine(INPUT)
current_pos = (0,0)
panels_painted = set()
facing_directions = {'N': (0,-1), 'S': (0,1), 'E': (1,0), 'W': (-1,0)}
current_heading = 'N'
grid = {}
grid[current_pos] = 1

def moveRobot(pos, dir):
    vector = facing_directions[dir]
    return (pos[0]+vector[0], pos[1]+vector[1])

def turnRobot(dir, spin):
    if dir == 'N':
        return 'W' if spin == 0 else 'E'
    elif dir == 'S':
        return 'E' if spin == 0 else 'W'
    elif dir == 'E':
        return 'N' if spin == 0 else 'S'
    elif dir == 'W':
        return 'S' if spin == 0 else 'N'

def getColor():
    if current_pos in grid:
        return grid[current_pos]
    else:
        return 0

def concatenate(l):
    s = ''
    for i in l:
        s += i
    return s


while True:
    current_color = getColor()
    #LOG.write(f"Currently at: {current_pos}, Color: {current_color}, Facing: {current_heading}\n")
    next_color = robot.run(current_color)
    #LOG.write(f"\tNext color: {next_color}\n")
    if not robot.is_running: # After the last input, before halting, the robot pauses. Need to check if it's halted
        print("DONE")
        break
    turn = robot.run(current_color)

    #LOG.write(f"\tTurn: {turn}\n")
    grid[current_pos] = next_color
    current_heading = turnRobot(current_heading, turn)
    #LOG.write(f"\tPainted here: {grid[current_pos]}, Turned toward: {current_heading}\n")
    current_pos = moveRobot(current_pos, current_heading)


cols, rows = zip(*grid.keys())
min_cols = -min(cols) if min(cols) < 0 else 0
min_rows = -min(rows) if min(rows) < 0 else 0
cols = [*map(lambda x: min_cols + x, cols)]
rows = [*map(lambda x: min_rows + x, rows)]
message = [[' ' for i in range(max(cols)+1)] for j in range(max(rows)+1)]
#LOG.write(f"min_rows: {min_rows}, min_cols: {min_cols}\n")
for k,v in grid.items():
    #LOG.write(f"{k[0]}, {k[1]}, {v}\n")
    message[k[1]+min_rows][k[0]+min_cols] = '#' if v == 1 else ' '
    #LOG.write(f"{k[0]}, {k[1]}, {v}, {message[k[1]+min_rows][k[0]+min_cols]}\n")

message = list(map(concatenate, message))
for line in message:
    LOG.write(line)
    LOG.write('\n')