# https://adventofcode.com/2019/day/1

def calcfuel(module):
    total = 0
    f = lambda x : int(x/3)-2
    fuel = f(module)
    while True:
        if fuel <= 0:
            return total
        else:
            total += fuel
            fuel = f(fuel)
        


print(sum(map(lambda x : calcfuel(int(x)), open('day1-input.txt','r').readlines())))
