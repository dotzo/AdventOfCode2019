# https://adventofcode.com/2019/day/12

from itertools import combinations, product
from functools import reduce
from math import gcd

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
            .format(*self.position, *self.velocity)

    @property
    def velocity(self):
        return (self.x_vel, self.y_vel, self.z_vel)

    @velocity.setter
    def velocity(self, *args):
        self.x_vel, self.y_vel, self.z_vel = args[0]

    @property
    def position(self):
        return (self.x_pos, self.y_pos, self.z_pos)

    @position.setter
    def position(self, *args):
        self.x_pos, self.y_pos, self.z_pos = args[0]

    @property
    def kinetic_energy(self):
        return sum(map(abs, self.velocity))

    @property
    def potential_energy(self):
        return sum(map(abs, self.position))

    @property
    def total_energy(self):
        return self.kinetic_energy * self.potential_energy

    @staticmethod
    def add(a,b,c,d,e,f):
        return (a+d, b+e, c+f)

    @staticmethod
    def compare(a,b):
            if a > b: return -1
            elif a < b: return 1
            else: return 0

    def updateVelocity(self, other):
        #print(f"Self: {self}, \nother: {other}")
        #print(Body.add(*self.velocity, *map(lambda x: Body.compare(*x), zip(self.position, other.position))))
        self.velocity = Body.add(*self.velocity, *map(lambda x: Body.compare(*x), zip(self.position, other.position)))
        #print(f"self velocity: {self.velocity}")

    def updatePosition(self):
        self.position = Body.add(*self.position, *self.velocity)

def parseInput(input):
    input = input.split('\n')
    for i in range(len(input)):
        input[i] = input[i][1:-1].split(',')
        for j in range(len(input[i])):
            sub = input[i][j]
            input[i][j] = int(sub[sub.index('=')+1:])

    return input


# INPUT = '''<x=-8, y=-10, z=0>
# <x=5, y=5, z=10>
# <x=2, y=-7, z=3>
# <x=9, y=-8, z=-3>'''
# INPUT = '''<x=-1, y=0, z=2>
# <x=2, y=-10, z=-7>
# <x=4, y=-8, z=8>
# <x=3, y=5, z=-1>'''
INPUT = open('day12-input.txt','r').read().strip()

# TIME_STEPS = 10

# bodies = [Body(*c) for c in parseInput(INPUT)]
# PAIRS_OF_BODIES = [*combinations(range(len(bodies)),2)]

# print(f"After 0 steps:")
# print(*bodies, sep = '\n')
# print('-----------------------------------')
# for t in range(TIME_STEPS):

#     # Step 1: calculate the gravity and update the velocities
#     for i,j in PAIRS_OF_BODIES:
#         bodies[i].updateVelocity(bodies[j])
#         bodies[j].updateVelocity(bodies[i])
#     # Step 2: Move all the bodies
#     for bod in bodies:
#         #print(bod)
#         bod.updatePosition()
    
#     # if not ((t+1)%100):
#     print(f"After {t+1} steps:")
#     print(*bodies, sep = '\n')
#     print('-----------------------------------')

# print(f"Energies after {TIME_STEPS} steps:")
# print(sum(bod.total_energy for bod in bodies))


####### 
# Part 2
# Each axis is operating independently, also each possible state has a unique previous state
# How the entire system updates creates a unique sequence for any given input
# As such we can simply run the entire simulation 3 times, once on each axis, and determine when
# it returns to the initial state.  The LCM of all 3 will be the state where the entire system returns to the start

def simulate(start, g=0):
    x = start
    dim = len(start)
    v = [0]*dim
    generation = 0
    while True:
        generation += 1
        for i in range(dim):
            v[i] += sum(map(lambda b: compare(x[i],b), x[:i] + x[i+1:]))
        x = [x[i] + v[i] for i in range(dim)]
        if x == start and v == [0]*dim:
            return generation
        
    # for t in range(g):
    #     for i in range(dim):
    #         v[i] += sum(map(lambda b: compare(x[i],b), x[:i] + x[i+1:]))
    #     x = [x[i] + v[i] for i in range(dim)]
    #     print(f"T: {t+1}, coord: {x}, vel: {v}")


def compare(a,b):
        if a > b: return -1
        elif a < b: return 1
        else: return 0

def lcm(*args):
    return reduce(lambda x,y: x*y//gcd(x,y), args[0])

dims = [*zip(*parseInput(INPUT))]
print(lcm([*map(lambda x: simulate([*x]), dims)]))
