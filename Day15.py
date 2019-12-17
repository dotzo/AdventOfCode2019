# https://adventofcode.com/2019/day/15

from util import filehelper as fh
from IntCode import IntComputer
from collections import defaultdict
import typing
from copy import copy
import time
import os

NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'

WALL = '#'
DROID = 'D'
OXYGEN = 'O'
FREE = '.'

OUTPUT_WALL = 0
OUTPUT_FREE = 1
OUTPUT_OXYGEN = 2

class Map:
    def __init__(self):
        self.data = defaultdict(str)
        self.position = (0,0)
        
    @classmethod
    def get_map(cls, program: typing.List[int], draw_mode=False) -> "Map":
        computer = IntComputer(program, wait_after_output=True, wait_for_input=True)
        visited = defaultdict(int)
        droid_map = Map()
        steps = 0
    
        while not computer.finished and steps < 6000:
            direction = droid_map.get_best_direction(visited)
            #direction = int(input('Input: '))
            steps += 1
            computer.inputs = [direction]
            computer.run()
            while not computer.waiting:
                computer.run()
            output = computer.output

            if output == OUTPUT_WALL:
                droid_map.wall_hit([NORTH, SOUTH, WEST, EAST][direction - 1])

            if output == OUTPUT_FREE:
                [droid_map.north, droid_map.south, droid_map.west, droid_map.east][direction - 1]()
                droid_map.set_position(droid_map.position, FREE)
            
            if output == OUTPUT_OXYGEN:
                [droid_map.north, droid_map.south, droid_map.west, droid_map.east][direction - 1]()
                droid_map.set_position(droid_map.position, OXYGEN)
            
            visited[droid_map.position] += 1
        
            if draw_mode:
                droid_map.render()

        return droid_map

    def get_best_direction(self, visited):
        # N, S, W, E
        all_dirs = [(0,1), (0, -1), (-1, 0), (1, 0)]

        for direction in all_dirs:
            new_pos = (self.position[0] + direction[0], self.position[1] + direction[1])
            if self.data[new_pos] != '':
                continue
                
            d = all_dirs.index(direction) + 1
            return d

        least_visited = 1e8
        least_dir = -1

        for direction in all_dirs:
            new_pos = (self.position[0] + direction[0], self.position[1] + direction[1])
            if self.data[new_pos] == WALL:
                continue
        
            if least_visited > visited[new_pos]:
                least_dir = direction
                least_visited = visited[new_pos]

        d = all_dirs.index(least_dir) + 1
        return d

    def north(self) -> None:
        self.position = (self.position[0], self.position[1] + 1)

    def south(self) -> None:
        self.position = (self.position[0], self.position[1] - 1)
        
    def west(self) -> None:
        self.position = (self.position[0] - 1, self.position[1])
        
    def east(self) -> None:
        self.position = (self.position[0] + 1, self.position[1])
        
    def set_position(self, coordinates: typing.Tuple[int, int], value: str) -> None:
        self.data[coordinates] = value

    def wall_hit(self, direction):
        x, y = self.position
        if direction == NORTH:
            self.set_position((x, y+1), WALL)
        elif direction == SOUTH:
            self.set_position((x, y-1), WALL)
        elif direction == WEST:
            self.set_position((x-1, y), WALL)
        elif direction == EAST:
            self.set_position((x+1, y), WALL)

    def find(self, value: str) -> typing.Tuple[int, int]:
        for k, v in self.data.items():
            if v == value:
                return k

    def get_border(self) -> typing.Tuple[int, int, int, int]:
        top, right, bottom, left = 0,0,0,0
        for position, value in self.data.items():
            if value:
                top = max(top, position[1])
                right = max(right, position[0])
                bottom = min(bottom, position[1])
                left = min(left, position[0])
        return top, right, bottom, left
    
    def find_oxygen(self) -> int:
        search = defaultdict(int)
        search[(0,0)] = 1
        new_search = copy(search)
        top, right, bottom, left = self.get_border()
        steps = 0

        while True:
            steps += 1
            
            for y in range(bottom, top+1):
                for x in range(left, right+1):
                    if search[(x,y)] == 1:
                        new_search[(x,y)] = -1
                        for direction in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                            new_pos = (x + direction[0], y + direction[1])
                            if search[new_pos] == -1:
                                continue
                            if self.data[new_pos] == FREE:
                                new_search[new_pos] = 1
                            if self.data[new_pos] == OXYGEN:
                                return steps

            search = copy(new_search)


    def fill_with_oxygen(self) -> int:
        search = defaultdict(int)
        search[self.find(OXYGEN)] = 1
        new_search = copy(search)
        top, right, bottom, left = self.get_border()
        steps = 0
        finished = False

        while not finished:
            finished = True
            for y in range(bottom, top + 1):
                for x in range(left, right+1):
                    if search[(x,y)] == 1:
                        new_search[(x,y)] = -1
                        for direction in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                            new_pos = (x + direction[0], y + direction[1])
                            if search[new_pos] == -1:
                                continue
                            if self.data[new_pos] == FREE:
                                new_search[new_pos] = 1
                                finished = False
            search = copy(new_search)
            steps += 1

        return steps - 1


    def render(self) -> None:
        time.sleep(0.01)
        top, right, bottom, left = self.get_border()
        # clear the terminal
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        for y in range(top, bottom-1, -1):
            for x in range(left, right+1):
                if self.position == (x,y):
                    print(DROID, end="")
                else:
                    print(self.data[(x,y)], end="")
                    if self.data[(x,y)] == '':
                        print(' ', end="")
            print()


def part_1():
    program = fh.csv_to_list('day15-input.txt')
    droid_map = Map.get_map(program)
    #droid_map.render()
    result = droid_map.find_oxygen()
    print(f"Number of steps to oxygen: {result}")

def part_2():
    program = fh.csv_to_list('day15-input.txt')
    droid_map = Map.get_map(program)
    result = droid_map.fill_with_oxygen()
    print(f"Number of minutes to fill with oxygen: {result}")

if __name__ == '__main__':
    part_1()
    part_2()