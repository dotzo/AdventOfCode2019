# https://adventofcode.com/2019/day/1

from util import filehelper as fh

modules = fh.lines_to_list('day1-input.txt')

def fuel(mass):
    return (mass // 3) - 2

def total_fuel(mass):
    next = fuel(mass)
    return 0 if next < 0 else next + total_fuel(next)







def part_1():
    return sum(map(fuel, modules))
def part_2():
    return sum(map(total_fuel, modules))
if __name__ == '__main__':
    print(f'The answer to part 1 is {part_1()}') #ans: 3456641
    print(f"The answer to part 2 is {part_2()}") #ans: 5182078