# https://adventofcode.com/2019/day/12

from itertools import combinations

class Body():
    def __init__(self, x, y, z):
        self.x_pos = x
        self.y_pos = y
        self.z_pos = z
        self.x_vel = 0
        self.y_vel = 0
        self.z_vel = 0

    def __str__(self):
        return "pos=<x={0:>6}, y={1:>6}, z={2:>6}>, vel=<x={3:>6}, y={4:>6}, z={5:>6}>"\
            .format(self.x_pos, self.y_pos, self.z_pos, self.x_vel, self.y_vel, self.z_vel)

    def updateVelocity(self, other):
        def compare(a,b):
            if a < b: return -1
            elif a > b: return 1
            else: return 0

        self.x_vel += compare(self.x_vel, other.x_vel)
        self.y_vel += compare(self.y_vel, other.y_vel)
        self.z_vel += compare(self.z_vel, other.z_vel)

    def updatePosition(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel
        self.z_pos += self.z_vel


INPUT = '''<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>'''

def parseInput(input):
    input = input.split('\n')
    for i in range(len(input)):
        input[i] = input[i][1:-1].split(',')
        for j in range(len(input[i])):
            sub = input[i][j]
            input[i][j] = int(sub[sub.index('=')+1:])

    return input

bodies = [Body(*c) for c in parseInput(INPUT)]

print(*bodies, sep = '\n')