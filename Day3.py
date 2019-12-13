# https://adventofcode.com/2019/day/3

from util import filehelper as fh

path1, path2 = [*map(lambda x: x.strip().split(','),fh.lines_to_list('day3-input.txt', str))]

def add(t1,t2):
    return (t1[0]+t2[0], t1[1]+t2[1])

def parse(s):
    d = {'R':(1,0), 'L':(-1,0), 'U':(0,1), 'D':(0,-1)}
    return (d[s[0]], int(s[1:]))

def makeWire(path):
    node = (0,0)
    nodes = []
    for i in path:
        direction, count = parse(i)
        for _ in range(0,count):
            node = add(node, direction)
            nodes.append(node)

    return nodes

def distance(p):
    return abs(p[0]) + abs(p[1])

def delay(w1, w2, p):
    return w1.index(p) + w2.index(p) + 2

def intersections(p,q):
    return list(set(p) & set(q))

wire1 = makeWire(path1)
wire2 = makeWire(path2)

def part_1():
    return min(map(distance, intersections(wire1, wire2)))

def part_2():
    return min(map(lambda p: delay(wire1, wire2, p), intersections(wire1, wire2)))

if __name__ == '__main__':
    print(f"The answer to part 1 is {part_1()}") # 2129
    print(f"The answer to part 2 is {part_2()}") # 134662