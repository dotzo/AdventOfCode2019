#https://adventofcode.com/2019/day/14

import math

class Nanofactory():
    def __init__(self, reactions):
        self.reactions = reactions
        self.surplus = {}

    def reset(self):
        self.surplus = {}

    def get_required_ore(self, material, amount):

        # 1:1 return, reached the end of the recursion
        if material == 'ORE':
            return amount

        # if I have surplus, use it
        if material in self.surplus:
            # I have enough to cover the cost, need no ore, use the surplus entirely
            if self.surplus[material] >= amount:
                self.surplus[material] -= amount
                return 0
            # I don't have enough, but use what i've got
            amount -= self.surplus[material]
        
        self.surplus[material] = 0

        reaction = self.reactions[material]
        multiplyer = math.ceil(amount / reaction['out'])

        out_amount = multiplyer * reaction['out']
        ore = 0

        for in_element, in_amount in reaction['inp'].items():
            ore += self.get_required_ore(in_element, multiplyer * in_amount)


        if out_amount > amount:
            self.surplus[material] += out_amount - amount


        return ore






INPUT = open('day14-input.txt','r').read().strip().split('\n')
# INPUT = '''157 ORE => 5 NZVS
# 165 ORE => 6 DCFZ
# 44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
# 12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
# 179 ORE => 7 PSHF
# 177 ORE => 5 HKGWZ
# 7 DCFZ, 7 PSHF => 2 XJWVT
# 165 ORE => 2 GPVTF
# 3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT'''.split('\n')

reactions = {}
for reaction in INPUT: # '7 A, 1 B => 1 C'
    reaction = reaction.split(' => ') # ['7 A, 1 B', '1 C']
    inp = {}
    for reactant in reaction[0].split(', '): # '7 A'
        reactant = reactant.split(' ') # ['7', 'A']
        inp[reactant[1]] = int(reactant[0])
    resultant = reaction[1].split(' ')
    reactions[resultant[1]] = {'inp': inp, 'out': int(resultant[0])}

#print(*reactions.items(), sep='\n')



def part_1():
    lab = Nanofactory(reactions)
    ore = lab.get_required_ore('FUEL', 1)
    #print(lab.surplus)
    return ore

def part_2():
    ore = 1000000000000
    lab = Nanofactory(reactions)
    
    upper = ore
    lower = math.ceil(upper / part_1())

    step = upper - lower
    num = lower
    res = 0
    req = 0
    #iter = 0
    while True:
        lab.reset()

        req = lab.get_required_ore('FUEL', num)
        #print(f"Ore required for {num} FUEL: {req}")

        step = step // 2
        #iter += 1
        if step < 1:
            break
        if req > ore:
            num -= step
        else:
            res = num
            num += step
    # lab.reset()
    # print (ore - lab.get_required_ore('FUEL',res))
    # print(lab.surplus)
    return res
if __name__ == '__main__':
    print(f"The answer to part 1 is {part_1()}") # 387001
    print(f"The answer to part 2 is {part_2()}") # 134662