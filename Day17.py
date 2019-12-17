# https://adventofcode.com/2019/day/17

from IntCode import IntComputer
from util import filehelper as fh

def part_1():
    program = fh.csv_to_list('day17-input.txt')
    ASCII = IntComputer(program, wait_after_output=True)

    screen = ''
    while not ASCII.finished:
        output = ASCII.run()
        screen += chr(output)

    screen = screen.strip().split('\n')
    intersections = []

    for row in range(1,len(screen)-1):
        for col in range(1,len(screen[row])-1):
            char = screen[row][col]
            if char != '#':
                continue
            else:
                if screen[row-1][col] == '#' and \
                    screen[row+1][col] == '#' and \
                    screen[row][col-1] == '#' and \
                    screen[row][col+1] == '#':
                    intersections.append((row, col))
    return sum([r*c for r,c in intersections])

def part_2():
    program = fh.csv_to_list('day17-input.txt')
    program[0] = 2
    ASCII = IntComputer(program, wait_after_output=False, wait_for_input=False)

    def to_ascii(l):
        return [ord(c) for c in l]

    # R, 8, R, 10, R, 10
    mov_func_A = ['R', ',', '8', ',', \
                    'R', ',', '1', '0', ',', \
                    'R', ',', '1', '0', '\n']
    mov_func_A = to_ascii(mov_func_A)

    # R, 4, R, 8, R, 10, R, 12
    mov_func_B = ['R', ',', '4', ',', \
                    'R', ',', '8', ',', \
                    'R', ',', '1', '0', ',', \
                    'R', ',', '1', '2', '\n']
    mov_func_B = to_ascii(mov_func_B)

    # R, 12, R, 4, L, 12, L, 12
    mov_func_C = ['R', ',', '1', '2', ',', \
                    'R', ',', '4', ',', \
                    'L', ',' ,'1', '2', ',',
                    'L', ',', '1', '2', '\n']
    mov_func_C = to_ascii(mov_func_C)

    # A, B, A, C, A, B, C, A, B, C
    main_func = ['A', ',', 'B', ',', \
                'A', ',', 'C', ',', \
                'A', ',', 'B', ',', \
                'C', ',', 'A', ',', \
                'B', ',', 'C', '\n']
    main_func = to_ascii(main_func)

    # y or n if you want to see a continuous feed of what's happening
    cont_feed = ['n', '\n']
    cont_feed = to_ascii(cont_feed)

    # input order: MAIN, MOV A, MOV B, MOV C, 
    ASCII.inputs = main_func + mov_func_A + mov_func_B + mov_func_C + cont_feed
    return ASCII.run()



if __name__ == '__main__':
    print(f"The solution to part 1 is {part_1()} .")
    print(f"The solution to part 2 is {part_2()} .")
