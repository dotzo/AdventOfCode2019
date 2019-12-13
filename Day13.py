# https://adventofcode.com/2019/day/13\\

from IntCode import IntComputer

EMPTY = 0
WALL = 1
BLOCK = 2
PADDLE = 3
BALL = 4

NO_MOVE = 0
LEFT = -1
RIGHT = 1

BLOCK_TYPES = {
    EMPTY: ' ',
    WALL: '#',
    BLOCK: '@',
    PADDLE: '_',
    BALL: 'o'
}


class Game:
    def __init__(self, program, play=True, visual_mode=False):
        if play:
            program[0] = 2
        self.computer = IntComputer(
            program, wait_after_output=True, wait_for_input=True
        )
        self.visual_mode = visual_mode
        self.game_map = {}
        self.score = None

    def render(self):
        last_row = 0
        # reset the terminal window
        print("\033c", end="")
        for y, x in sorted(self.game_map.keys()):
            if last_row != y:
                print("")
            print(BLOCK_TYPES[self.game_map[(y,x)]], end="")
            last_row = y
        print("")

    def play_game(self):
        n = 0
        current_x = None
        current_y = None
        ball_x = None
        paddle_x = None
        while not self.computer.finished:
            n += 1
            output = self.computer.run()
            ready = not self.computer.finished and not self.computer.waiting
            if self.computer.waiting: #waiting for input
                if paddle_x < ball_x:
                    i = RIGHT
                elif paddle_x > ball_x:
                    i = LEFT
                else:
                    i = NO_MOVE
                self.computer.inputs = [i]
                if self.visual_mode:
                    self.render()
                n -= 1 #reset to rerun with above input

            elif ready and n == 1:
                current_x = output
            elif ready and n == 2:
                current_y = output
            elif ready and n == 3:
                if current_x == -1 and current_y == 0:
                    self.score = output
                else:
                    current_tile == output
                    self.game_map[(current_y, current_x)] = current_tile
                    if current_tile == 4: #ball
                        ball_x = current_x
                    if current_tile == 3: #paddle
                        paddle_x = current_x
                n = 0


def part_1():
    with open('day13-input.txt','r') as f:
        program = [*map(int, f.read().split(','))]

    game = Game(program, play=False, visual_mode=True)
    game.play_game()

    count = 0

    for item in game.game_map:
        if game.game_map[item] == BLOCK:
            count += 1

    print(f"Total Blocks: {count}")

if __name__ == "__main__":
    part_1()