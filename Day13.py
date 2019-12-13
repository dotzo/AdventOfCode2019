# https://adventofcode.com/2019/day/13\\

from IntcodeComputer import Machine

INPUT = open('day13-input.txt','r').read()
INPUT = list(map(int, INPUT.split(',')))

HEIGHT = 100
WIDTH = 100

board = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]

game = Machine(INPUT, wait_after_output=True, wait_for_input=True)
# set addr 0 to 2 for free to play mode
game.play_game()

n = 0
current_x = None
current_y = None
ball_x = None
paddle_x = None
score = 0
while not game.finished:
    n += 1
    output = game.run()
    ready = not game.finished and not game.waiting
    if game.waiting: #waiting for input
        if paddle_x < ball_x:
            i = 1
        elif paddle_x > ball_x:
            i = -1
        else:
            i = 0
        game.inputs = [i]

        n -= 1 #reset to rerun with above input
    elif ready and n == 1:
        current_x = output
    elif ready and n == 2:
        current_y = output
    elif ready and n == 3:
        if current_x == -1 and current_y == 0:
            score = output
        else:
            board[current_y][current_x] == output

            if output == 4: #ball
                ball_x = current_x
            if output == 3: #paddle
                paddle_x = current_x
        n = 0


print(score)