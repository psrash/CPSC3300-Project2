import sys

# Model Classes
class Memory:
    def __init__(self):
        self.memory = {}
        self.read_count = 0
        self.write_count = 0

    def read(self):
        pass
    
    def write():
        pass

class Register:
    def __init__(self):
        self.register = [0] * 32 # just to initialize

class PC:
    def __init__(self):
        pass   

class ALU:
    def __init__(self):
        # Track count of each ALU operation
        self.operation_count = {
            'add': 0,
            'sub': 0,
            'and': 0,
            'or': 0,
            'slt': 0,
        }

class CPU:
    def __init__(self):
        self.memory = Memory()  # store instructions and data
        self.registers = Register()  # hold data
        self.program_counter = 0  # current instruction address
        self.instruction_count = {
            'add': 0,
            'addi': 0,
            'sub': 0,
            'and': 0,
            'or': 0,
            'slt': 0,
            'beq': 0,
            'j': 0,
            'lw': 0,
            'sw': 0
        }
        self.cycles = 0  # track the number of cycles executed

    def readRType(self, instruction):
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
        #TODO check what funct it is and proccess based on that

    def readIType(self, instruction):
        op = (instruction >> 26) & 0x3F
        rs = (instruction >> 21) & 0x1F
        rt = (instruction >> 16) & 0x1F
        immediate = instruction & 0xFFFF
        #TODO check what op it is and proccess based on that

    def readJType(instruction):
        op = (instruction >> 26) & 0x3F
        address = instruction & 0x3FFFFFF
        #TODO check what op it is and proccess based on that

# Controller 
class Controller:
    def __init__(self, cpu, view):
        self.cpu = cpu
        self.view = view

    def readInFile(self, filename):
        in_file = open(filename, "rb")
        raw_data = in_file.read(4)
        instruction = int.from_bytes(raw_data, byteorder='big')

        for i in range(31, -1, -1):
            bit = (instruction >> i) & 1
            print(bit, end='')
        print('\n')

        op = (instruction >> 26) & 0b111111
        print(f"The operand is: {op:06b}")
        # check what operand it is and based on that process that instruction format
        if op == 0:
            self.cpu.readRType(instruction)
        elif op == 35 or op == 43:
            self.cpu.readJType(instruction)
        else:
            self.cpu.readIType(instruction)

    def run_program(self):
        # Logic to execute the instruction
        self.cpu.program_counter += 1
        self.view.output()

# View
class View:
    def __init__(self, cpu):
        self.cpu = cpu

    def output(self):
        pass



def main():
    cpu = CPU()
    view = View(cpu)
    controller = Controller(cpu, view)
    filename = sys.argv[1]
    controller.readInFile(filename)

if __name__ == "__main__":
    main()
else:
    print("program failed")