# https://adventofcode.com/2019/day/15

from IntCode import IntComputer
from util import filehelper as fh
from operator import itemgetter
from random import choice

program = fh.csv_to_list('day15-input.txt')

BLOCK_TYPES = {
    'WALL': '#',
    'VISITED': '.',
    'BOT': 'D',
    'UNK': ' ',
    'GOAL': 'X',
    'START': 'O',
    'DEAD': '@'
}

move_direction = {
    'N': {'bot_input': 1, 'vector': (0, -1)},
    'S': {'bot_input': 2, 'vector': (0, 1)},
    'W': {'bot_input': 3, 'vector': (-1, 0)},
    'E': {'bot_input': 4, 'vector': (1, 0)}
}

def opposite(dir):
    if dir == 'N': return 'S'
    elif dir == 'S': return 'N'
    elif dir == 'E': return 'W'
    elif dir == 'W': return 'E'

def add(a,b):
        return (a[0]+b[0], a[1] + b[1])

class Robot():
    def __init__(self, program, visual_mode = False, manual_mode = False):
        self.robot = IntComputer(program, wait_after_output=True, wait_for_input=True)
        self.visual_mode = visual_mode
        self.manual_mode = manual_mode
        self._HEIGHT = 25
        self._WIDTH = 25
        self.starting_pos = (0,0)
        self.current_pos = self.starting_pos
        self.goal_pos = None
        self.map = {(x,y): 'UNK' for x in range(-self._WIDTH, self._WIDTH) for y in range(-self._HEIGHT,self._HEIGHT)}
        self.map[self.current_pos] = 'BOT'
        self.junctions = set()
        self.moves = []
        
    
    def render(self):
        last_row = 0
        # reset the terminal window
        print("\033c", end="")
        for x, y in sorted(self.map.keys(), key=itemgetter(1)):
            if last_row != y:
                print("")
            print(BLOCK_TYPES[self.map[(x,y)]], end="")
            last_row = y
        print("")

    def look_around(self):
        res = []
        for dir in ['N', 'S', 'W', 'E']:
            self.robot.inputs = [move_direction[dir]['bot_input']]
            vector = move_direction[dir]['vector']
            test_location = add(self.current_pos, vector)
            if self.map[test_location] != 'UNK':
                continue
            output = self.robot.run()
            if output == 0:
                self.map[test_location] = 'WALL'
            else:
                self.robot.inputs = [move_direction[opposite(dir)]['bot_input']]
                self.robot.run()
                res.append(dir)
        return res

    def move_robot(self, direction, backtracking=False):
        bot_input = move_direction[direction]['bot_input']
        vector = move_direction[direction]['vector']
        self.robot.inputs = [bot_input]
        output = self.robot.run()
        
        if output == 2:
            self.goal_pos = self.current_pos
            self.map[self.current_pos] = 'GOAL'
        else:
            self.map[self.current_pos] = 'VISITED' if not backtracking else self.map[self.current_pos]
            self.current_pos = add(self.current_pos, vector)
            self.map[self.current_pos] = 'BOT'
        

    def start(self):
        while self.current_pos != self.goal_pos:
            if self.visual_mode:
                self.render()
                # print(self.moves[-1:-20:-1])
                # print(self.junctions)
            user_input = None
            if self.manual_mode:
                user_input = input("Dir to Move: ")
                if user_input not in move_direction:
                    user_input = input("Dir to Move: ")
                    continue
            else: 
                possible_directions = self.look_around()
                if len(possible_directions) == 0:
                    if len(self.junctions) > 0:
                        self.map[self.current_pos] = 'DEAD'
                        while self.current_pos not in self.junctions:
                            #self.render()
                            #print(self.moves[-1:-10:-1])
                            self.move_robot(opposite(self.moves.pop(-1)))
                        continue
                    else:
                        self.map[self.starting_pos] = 'START'
                        self.map[self.goal_pos] = 'GOAL'
                        break
                elif len(possible_directions) == 1:
                    user_input = possible_directions[0]
                    self.junctions.discard(self.current_pos)
                else:
                    user_input = choice(possible_directions)
                    self.junctions.add(self.current_pos)

            self.move_robot(user_input)
            self.moves.append(user_input)
            

            

bot = Robot(program, visual_mode=False)
bot.start()
bot.render()
print(f"We started at {bot.starting_pos}, the goal is at {bot.goal_pos}.")
print(f"It took {len(bot.moves)} to get here.")

#print(bot.map)

