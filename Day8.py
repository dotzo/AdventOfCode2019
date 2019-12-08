# https://adventofcode.com/2019/day/8

# WIDTH = 2
# HEIGHT = 2
# INPUT = '0222112222120000'

WIDTH = 25
HEIGHT = 6
INPUT = open('day8-input.txt','r').read().strip()

LENGTH = len(INPUT)
DEPTH = LENGTH//(WIDTH*HEIGHT)

def splitString(s, n):
    L = len(s)
    r = []
    for i in range(n):
        sec = L // n
        r.append(s[i*sec : (i+1)*sec])
    return r

def countDigits(s, d):
    return len(list(filter(lambda x: x == d, s)))

layers = splitString(INPUT, DEPTH)


final_image = []
for i in range(WIDTH*HEIGHT):
    test = []
    for j in range(DEPTH):
        test.append(int(layers[j][i]))
    final_image.append(list(filter(lambda x: x != 2, test))[0])

for row in splitString(final_image, HEIGHT):
    print(row)