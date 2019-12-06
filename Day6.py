# https://adventofcode.com/2019/day/6

input = open('day6-input.txt','r').readlines()

# input = '''COM)B
# B)C
# C)D
# D)E
# E)F
# B)G
# G)H
# D)I
# E)J
# J)K
# K)L
# K)YOU
# I)SAN'''.splitlines()

# x)y -> y directly orbits x -> orbits[y] = x
orbits = {}
for i in input:
    a,b = i.split(')')
    orbits[b.strip()] = a

def pathToDest(p, dest = 'COM'):
    if dest == 'COM':
        if orbits[p] == dest: 
            return [p, orbits[p]]
        else: 
            return [p] + pathToDest(orbits[p], dest)
    else:
        a = pathToDest(p)
        b = pathToDest(dest)
        a.reverse()
        b.reverse()
        for i in range(min(len(a), len(b))):
            if a[i] != b[i]:
                return list(reversed(a[i:])) + b[i-1:]

def distToDest(path):
    if path[-1] == 'COM':
        return len(path) - 1
    else:
        return len(path) - 3

print(distToDest(pathToDest('YOU','SAN')))