import sys

# Model Classes
class Memory:
    def __init__(self):
        self.memory = {}

    def read():
        pass
    
    def write():
        pass

class Register:
    def __init__(self):
        self.register = [0] * 32 # just to initialize

class PC:
    def __init__(self):
        pass   

class CPU:
    def __init__(self):
        self.memory = Memory()  # store instructions and data
        self.registers = Register()  # hold data
        self.program_counter = 0  # current instruction address
        self.instruction_count = {
            'add': 0, # Extend with other instructions as needed
        }
        self.cycles = 0  # track the number of cycles executed

# Controller 
class Controller:
    def __init__(self, cpu, view):
        self.cpu = cpu
        self.view = view

    def is_halted(self):
        # This should check if the program should stop, like reaching a HALT instruction
        return False

    def execute_cycle(self):
        # Fetch, decode, and execute an instruction
        instruction = self.cpu.memory.read(self.cpu.program_counter)
        # Logic to execute the instruction
        self.cpu.program_counter += 1
        self.view.update()

    def run_program(self):
        # Runs the entire program without stopping
        while not self.is_halted():
            self.execute_cycle()

    def single_step(self):
        # Runs one instruction at a time, waiting for user input
        while not self.is_halted():
            input("Press Enter to execute the next instruction...")
            self.execute_cycle()

# View
class View:
    def __init__(self, cpu_model):
        self.cpu = cpu_model

def readRType(instruction):
    #get operand
    op = (instruction >> 26) & 0x3F
    print(f"The operand is: {op:06b}")
    rs = (instruction >> 21) & 0x1F
    print(f"The rs register is: {rs:05b}")
    rt = (instruction >> 16) & 0x1F
    print(f"the rt register is: {rt:05b}")
    rd = (instruction >> 11) & 0x1F
    print(f"the rd register is: {rd:05b}")
    shamt = (instruction >> 6) & 0x1F
    print(f"the shamt is: {shamt:05b}")
    funct = instruction & 0x3F
    print(f"the function is: {funct:06b}")


def readInFile(filename):
    in_file = open(filename, "rb")
    raw_data = in_file.read(4)
    instruction = int.from_bytes(raw_data, byteorder='big')

    for i in range(31, -1, -1):
        bit = (instruction >> i) & 1
        print(bit, end='')
    print('\n')

    op = (instruction >> 26) & 0b111111
    print(f"The operand is: {op:06b}")
    #check what operand it is and based on that process that instruction format
    readRType(instruction)

def main():
    filename = sys.argv[1]
    readInFile(filename)

if __name__ == "__main__":
    main()
else:
    print("program failed")