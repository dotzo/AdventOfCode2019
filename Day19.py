# https://adventofcode.com/2019/day/19

from util import filehelper as fh
from IntCode import IntComputer
from collections import defaultdict

program = fh.csv_to_list('day19-input.txt')

def part_1():
    total_pull_nodes = 0
    graph = ''


    for y in range(50):
        for x in range(50):
            bot = IntComputer(program, wait_for_input=False, wait_after_output=False)
            bot.inputs = [x,y]
            output = bot.run()
            total_pull_nodes += output
            graph += '#' if output == 1 else '.'
        
        graph += '\n'

    print(graph)
    print(f"The total number of nodes that pull is: {total_pull_nodes} .")

def part_2():
    grid = defaultdict(lambda _: '.')
    dim = 100
    cur_x, cur_y = 100, 100
    while True:
        # Do the corner
        bot = IntComputer(program, wait_for_input=False, wait_after_output=False)
        bot.inputs = [cur_x, cur_y]
        grid[(cur_x, cur_y)] = '#' if bot.run() else '.'
        del bot

        # do the edges
        for i in range(1,dim):
                bot_x = IntComputer(program, wait_for_input=False, wait_after_output=False)
                bot_y = IntComputer(program, wait_for_input=False, wait_after_output=False)
                bot_x.inputs = [cur_x - i, cur_y]
                bot_y.inputs = [cur_x, cur_y - i]
                grid[(cur_x - i, cur_y)] = '#' if bot_x.run() else '.'
                grid[(cur_x, cur_y - i)] = '#' if bot_y.run() else '.'
                del bot_x, bot_y

        #Check if we've achieved our goal
        for coord, state in grid.items():
            if coord[1] < 100:
                continue
            #start from a tractor spot, check that it's on the left edge,
            #go up and right 100 units to find the other corner and make sure it's a tractor spot, 
            #and make sure that spot is a right edge
            if grid[coord] == '#' \
                and grid[(coord[0] - 1, coord[1])] == '.' \
                and grid[(coord[0] + 100, coord[1] - 100)] == '#' \
                and grid[(coord[0] + 101, coord[1] - 100)] == '.':
                return 10000* coord[0] + (coord[1] - 100)
        cur_x += 1
        cur_y += 1
        dim += 1

print(part_2())