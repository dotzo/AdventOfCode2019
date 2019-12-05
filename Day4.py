# https://adventofcode.com/2019/day/4

INPUT = '137683-596253'

def meetsCriteria(n):
    s = list(map(int,str(n)))
    countAdjs = [0]*10
    hasMonotone = True
    for d in range(len(s)-1):
        a = s[d]
        b = s[d+1]
        countAdjs[a] += 1 if (a == b) else 0
        hasMonotone = hasMonotone and (a <= b)
    


    return any(filter(lambda x: x == 1, countAdjs)) and hasMonotone
        
    

count = 0
for i in range(137683,596253):
    count += 1 if meetsCriteria(i) else 0

print(count)