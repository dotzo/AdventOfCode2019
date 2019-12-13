import sys
import copy
class Machine:
    def __init__(self, 
        data, 
        pointer = 0,
        inputs = [],
        wait_after_output = False, 
        wait_for_input = False):
        self.data = copy.deepcopy(data)
        self.limit = len(self.data)
        self.memory = {}
        self.inputs = inputs
        self.output = -1
        self.IP = pointer
        self.RB = 0 #Relative base used for relative mode, set by opcode 9
        self.finished = False
        self.waiting = False
        self.wait_after_output = wait_after_output
        self.wait_for_input = wait_for_input

    def run(self):
        self.waiting = False
        while not self.finished:

            cmd = self.data[self.IP] % 100

            if cmd == 99: #program is done
                self.waiting = True
                self.finished = True
                return self.output
            elif cmd == 3 and len(self.inputs) == 0 and self.wait_for_input: #input
                #LOG.write(f"\t--using input: {input}\n")
                self.waiting = True
                return None
            else:
                
                if cmd == 1: #add
                    self.set_param(3, self.param(1) + self.param(2))
                    self.IP += 4
                elif cmd == 2: #multiply
                    self.set_param(3, self.param(1) * self.param(2))
                    self.IP += 4
                elif cmd == 3: 
                    self.set_param(1, self.get_input())
                    self.IP += 2
                elif cmd == 4: #output
                    self.output = self.param(1)
                    #LOG.write(f"\t--output: {output}\n")
                    self.IP += 2
                    if self.wait_after_output:
                        return self.output
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
                elif cmd == 9: #adj_relative_base
                    self.RB += self.param(1)
                    self.IP += 2
                else: #error
                    print(f"unknown opcode: {self.data[self.IP]}")
                    sys.exit(-1)
        return -1

    @property
    def is_running(self):
        return self.data[self.IP] != 99

    def get_input(self):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        else:
            return int(input("Input: "))

    def to_memory(self, addr, val):
        self.memory[addr] = val

    def from_memory(self, addr):
        if addr in self.memory:
            return self.memory[addr]
        else:
            return 0
    
    def param(self, n):
        mode = (self.data[self.IP] // (10**(n+1))) % 10
        if mode == 0: #position mode
            addr = self.data[self.IP+n]
            if addr >= self.limit:
                return self.from_memory(addr)
            else:
                return self.data[addr]
        elif mode == 1: #immediate mode
            return self.data[self.IP+n]
        else: #relative mode
            addr = self.RB + self.data[self.IP+n]
            if addr >= self.limit:
                return self.from_memory(addr)
            else:
                return self.data[addr]

    def set_param(self, n, val):
        mode = (self.data[self.IP] // (10**(n+1))) % 10
        if mode == 0: #position mode
            addr = self.data[self.IP+n]
            if addr >= self.limit:
                self.to_memory(addr, val)
            else:
                self.data[addr] = val
        elif mode == 1: #immediate mode
            self.data[self.IP+n] = val
        else: #relative mode
            addr = self.RB + self.data[self.IP+n]
            if addr >= self.limit:
                self.to_memory(addr, val)
            else:
                self.data[addr] = val

    # Used for day 7
    def phase_setup(self, n):
        self.set_param(1, n)
        self.IP += 2

    # Used for day 13
    def play_game(self):
        self.data[0] = 2