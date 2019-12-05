FILE = 'day5-input.txt'
BASE_STATE = list(map(int,open(FILE,'r').read().split(',')))
OOB = len(BASE_STATE)
def program(*args, return_address=0):
    memory = list(BASE_STATE)    
    for (a,v) in args:
        memory[a] = v
    COUNTER = 0

    def execute(count):
        opparams = memory[count]
        opcode = opparams % 100
        params = int('0b' + str((opparams - opcode) // 100),2)

        def getValue(value, mask):
            return memory[value] if params & mask == 0 else value

        # Takes 2 arguments and returns their sum to the third address
        if opcode == 1:
            _, a1, a2, ra = memory[count:count+4]
            memory[ra] = getValue(a1,1) + getValue(a2,2)
            return count+4

        # Takes 2 arguments and returns their product to the third address
        elif opcode == 2:
            _, a1, a2, ra = memory[count:count+4]
            memory[ra] = getValue(a1,1) * getValue(a2,2)
            return count+4
        
        # Takes a user input and stores it at the address given
        elif opcode == 3:
            _, ra = memory[count:count+2]
            memory[ra] = int(input("Input a number: "))
            return count+2
        
        # Outputs the value at the parameter address
        elif opcode == 4:
            _, addr = memory[count:count+2]
            print("Test: " + str(getValue(addr,1)))
            return count+2
        
        # If first argument is not 0, set count to 2nd number, else nothing
        elif opcode == 5:
            _, addr, ra = memory[count:count+3]
            addr = getValue(addr,1)
            if addr != 0:
                return getValue(ra,2)
            else:
                return count+3

        # If first argument is 0, set count to 2nd number, else nothing
        elif opcode == 6:
            _, addr, ra = memory[count:count+3]
            addr = getValue(addr,1)
            if addr == 0:
                return getValue(ra,2)
            else:
                return count+3

        # Returns 1 if a < b, 0 otherwise
        elif opcode == 7:
            _, a1, a2, ra = memory[count:count+4]
            memory[ra] = 1 if (getValue(a1,1) < getValue(a2,2)) else 0
            return count+4

        # Returns 1 if a == b, 0 otherwise
        elif opcode == 8:
            _, a1, a2, ra = memory[count:count+4]
            memory[ra] = 1 if (getValue(a1,1) == getValue(a2,2)) else 0
            return count+4

        # Halts the program
        elif opcode == 99:
            return -1
        else: return -2
    
    while COUNTER < OOB:
        r = execute(COUNTER)
        if r == -1:
            if return_address == -1:
                print("Program has halted.")
                return None
            else:
                return memory[return_address]
        else:
            COUNTER = r
    else:
        return -1