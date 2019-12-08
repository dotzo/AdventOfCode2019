import sys
import copy

class Machine:
    def __init__(self, data):
        self.data = copy.deepcopy(data)
        self.IP = 0


    def run(self, input):
        while self.data[self.IP] != 99:

            cmd = self.data[self.IP] % 100

            if cmd == 1: #add
                self.set_param(3, self.param(1) + self.param(2))
                self.IP += 4
            elif cmd == 2: #multiply
                self.set_param(3, self.param(1) * self.param(2))
                self.IP += 4
            elif cmd == 3: #input
                #print(f"using input: {input}")
                self.set_param(1, input)
                self.IP += 2
            elif cmd == 4: #output
                output = self.param(1)
                #print(f"output: {output}")
                self.IP += 2
                return output
            elif cmd == 5: #jump_if_true
                self.IP = self.param(2) if self.param(1) != 0 else self.IP + 3
            elif cmd == 6: #jump_if_false
                self.IP = self.param(2) if self.param(1) == 0 else self.IP + 3
            elif cmd == 7: #less_than
                self.set_param(3, 1 if self.param(1) < self.param(2) else 0)
                self.IP += 4
            elif cmd == 8: #equals
                self.set_param(3, 1 if self.param(1) == self.param(2) else 0)
                self.IP += 4
            else: #error
                print(f"unknown opcode: {self.data[self.IP]}")
                sys.exit(-1)
        return 0

    @property
    def is_running(self):
        return self.data[self.IP] != 99

    def param(self, n):
        if (self.data[self.IP] // (10**(n+1))) % 10 == 0:
            return self.data[self.data[self.IP+n]]
        else:
            return self.data[self.IP+n]

    def set_param(self, n, val):
        if (self.data[self.IP] // (10**(n+1))) % 10 == 0:
            self.data[self.data[self.IP+n]] = val
        else:
            self.data[self.IP+n] = val

    # Used for day 7
    def phase_setup(self, n):
        self.set_param(1, n)
        self.IP += 2