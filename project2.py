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

    def run_program(self):
        # Logic to execute the instruction
        self.cpu.program_counter += 1
        self.view.output()

# View
class View:
    def __init__(self, cpu_model):
        self.cpu = cpu_model

    def output(self):
        pass

def readRType(instruction):
    #get operand
    op = (instruction >> 26) & 0x3F
    print(f"The operand is: {op:06b}")
    rs = (instruction >> 21) & 0x1F
    print(f"The rs register is: {rs}")
    rt = (instruction >> 16) & 0x1F
    print(f"the rt register is: {rt}")
    rd = (instruction >> 11) & 0x1F
    print(f"the rd register is: {rd}")
    shamt = (instruction >> 6) & 0x1F
    print(f"the shamt is: {shamt}")
    funct = instruction & 0x3F
    print(f"the function is: {funct}")

def readIType(instruction):
    op = (instruction >> 26) & 0x3F
    rs = (instruction >> 21) & 0x1F
    rt = (instruction >> 16) & 0x1F
    immediate = instruction & 0xFFFF


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