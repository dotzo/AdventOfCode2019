# https://adventofcode.com/2019/day/3

path1, path2 = list(map(lambda x: x.split(','), open('day3-input.txt','r').readlines()))

def add(t1,t2):
    return (t1[0]+t2[0], t1[1]+t2[1])

def parse(s):
    d = {'R':(1,0), 'L':(-1,0), 'U':(0,1), 'D':(0,-1)}
    return (d[s[0]], int(s[1:]))

