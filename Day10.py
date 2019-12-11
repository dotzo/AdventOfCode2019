# https://adventofcode.com/2019/day/10

from fractions import Fraction
from math import atan2, hypot, pi

INPUT = open('day10-input.txt','r').readlines()
# INPUT = '''.#..##.###...#######
# ##.############..##.
# .#.######.########.#
# .###.#######.####.#.
# #####.##.#.##.###.##
# ..#####..#.#########
# ####################
# #.####....###.#.#.##
# ##.#################
# #####.##.###..####..
# ..######..##.#######
# ####.##.####...##..#
# .#####..#.######.###
# ##...#.##########...
# #.##########.#######
# .####.#.###.###.#.##
# ....##.##.###..#####
# .#.#.###########.###
# #.#.#.#####.####.###
# ###.##.####.##.#..##'''.split('\n')
coords = []
for y in range(len(INPUT)):
    for x in range(len(INPUT[y])):
        if INPUT[y][x] == '#':
            coords.append([x,y])

def vector(a,b):
    a1, a2 = a
    b1, b2 = b
    dist = abs(b1 - a1) + abs(b2 - a2)
    if dist == 0:
        return (0,0)
    else:
        return (Fraction(b1 - a1, dist), Fraction(b2 - a2, dist))

def numberVisible(test, field):
    s = set()
    for asteroid in field:
        s.add(vector(test, asteroid))
    #print(s)
    return len(s) - 1 # subtract 1 to account for when test == asteroid




station = max(coords, key=lambda x: numberVisible(x,coords))
print(f"The winner is {station} with {numberVisible(station, coords)} visible asteroids.")
newcoords = list(map(lambda x: [x[0] - station[0], station[1] - x[1]], coords))
# Calculates the clockwise angle and distince from the station to a point relative to the vector (0,1)
# representing the starting point of the laser
ref = (0,1)
def clockwiseangle_and_distance(point):
    vector = point
    lenvector = hypot(vector[0], vector[1])
    if lenvector == 0:
        return -pi, 0
    normalized = (vector[0]/lenvector, vector[1]/lenvector)
    dotprod = normalized[0]*ref[0] + normalized[1]*ref[1]
    diffprod = ref[1]*normalized[0] - ref[0]*normalized[1]
    angle = atan2(diffprod, dotprod)
    if angle < 0:
        return 2*pi+angle, lenvector
    return angle, lenvector

def groupby_angle(input):
    grouped = [[input[0]]]
    previous = clockwiseangle_and_distance(input[0])[0]
    grouping = 0
    for i in input[1:]:
        new = clockwiseangle_and_distance(i)[0]
        if  new == previous:
            grouped[grouping].append(i)
        else:
            grouped.append([i])
            grouping += 1
        previous = new
    return grouped

targets = groupby_angle(sorted(newcoords, key=clockwiseangle_and_distance))
vaporized = [targets.pop(0)[0]]
while targets:
    for grouping in targets:
        next = grouping.pop(0)
        vaporized.append([next[0] + station[0], station[1] - next[1]])
    targets = list(filter(lambda x: x != [], targets))

print(f"The coordinates of the 200th asteroid are {vaporized[200]}.")
print(f"The answer to the puzzle is {vaporized[200][0]*100+vaporized[200][1]}")