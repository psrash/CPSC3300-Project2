import sys

# Model Classes
class Memory:
    def __init__(self):
        self.memory = {}
        self.read_count = 0
        self.write_count = 0

    def read(self, address):
        self.read_count += 1
        return self.memory.get(address, 0)  # Return 0 if the address is not in memory

    def write(self, address, value):
        self.write_count += 1
        self.memory[address] = value

class Register:
    def __init__(self):
        self.register = [0] * 32 # just to initialize

class PC:
    def __init__(self):
        self.value = 0

    def increment(self):  # Default step for 4-byte instructions
        self.value += 4

    def set_address(self, address):
        self.value = address 

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
        self.program_counter = PC()  # current instruction address
        self.alu = ALU()
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
        self.cycles = 1  # track the number of cycles executed

    def readRType(self, instruction):
        print("R type")
        #get operand
        op = (instruction >> 26) & 0x3F
        rs = (instruction >> 21) & 0x1F
        rt = (instruction >> 16) & 0x1F
        rd = (instruction >> 11) & 0x1F
        shamt = (instruction >> 6) & 0x1F
        funct = instruction & 0x3F
        #TODO check what funct it is and proccess based on that
        if funct == 32:
            self.alu.operation_count['add'] += 1
            self.instruction_count['add'] += 1
        elif funct == 34:
            self.alu.operation_count['sub'] += 1
            self.instruction_count['sub'] += 1
        elif funct == 36:
            self.alu.operation_count['and'] += 1
            self.instruction_count['and'] += 1
        elif funct == 37:
            self.alu.operation_count['or'] += 1
            self.instruction_count['or'] += 1
        elif funct == 42:
            self.alu.operation_count['slt'] += 1
            self.instruction_count['slt'] += 1
        else:
            print("invalid function")


    def readIType(self, instruction):
        print("I Type")
        op = (instruction >> 26) & 0x3F
        rs = (instruction >> 21) & 0x1F
        rt = (instruction >> 16) & 0x1F
        immediate = instruction & 0xFFFF
        #TODO check what op it is and proccess based on that
        if op == 4:
            if self.registers.register[rs] == self.registers.register[rt]:
                self.instruction_count['beq'] += 1
                offset = immediate << 2
                print (offset)
                self.program_counter.set_address(self.program_counter.value + offset)
        elif op == 8:
            self.instruction_count['addi'] += 1
        elif op == 35:
            self.instruction_count['lw'] += 1
        elif op == 43:
            self.instruction_count['sw'] += 1

    def readJType(instruction):
        print("J type")
        # Always going to be jump operand
        op = (instruction >> 26) & 0x3F
        address = instruction & 0x3FFFFFF

# Controller 
class Controller:
    def __init__(self, cpu, view):
        self.cpu = cpu
        self.view = view

    def read_file(self, filename):
        in_file = open(filename, "rb")
        address = 0  # Start at memory address 0
        raw_data = in_file.read(4)
        while raw_data:
            instruction = int.from_bytes(raw_data, byteorder='big')
            
            # Store the instruction in memory at the current address
            self.cpu.memory.write(address, instruction)
            
            # Print the instruction as binary
            for i in range(31, -1, -1):
                bit = (instruction >> i) & 1
                print(bit, end='')
            print('\n')
            
            # Increment address by 4 for next instruction
            address += 4
            raw_data = in_file.read(4)


    def run_program(self):
        while self.cpu.program_counter.value in self.cpu.memory.memory:
            # Fetch the instruction from memory at the address pointed to by the program counter
            address = self.cpu.program_counter.value
            instruction = self.cpu.memory.read(address)  # Fetch the instruction
            
            # Decode the opcode
            op = (instruction >> 26) & 0x3F
            
            # Process the instruction based on its type
            if op == 0:  # R-Type instructions have opcode 0
                self.cpu.readRType(instruction)
            elif op == 2:  # J-Type instruction for 'j'
                self.cpu.readJType(instruction)
            else:  # I-Type instructions
                self.cpu.readIType(instruction)
            
            # Increment the program counter normally unless it's a jump or branch
            if op not in (2, 4):  # Assuming `op == 2` is a jump and `op == 4` is a branch
                self.cpu.program_counter.increment()
            
            # Output the state after each instruction
            self.view.output()
            
            # Increment the cycle count after processing each instruction
            self.cpu.cycles += 1


# View
class View:
    def __init__(self, cpu):
        self.cpu = cpu

    def output(self):
        print("PC:", self.cpu.program_counter.value)
        print("Registers:", self.cpu.registers.register)
        print("Memory Accesses: Reads:", self.cpu.memory.read_count, "Writes:", self.cpu.memory.write_count)
        print("Instruction Counts:", self.cpu.instruction_count)
        print("ALU Operations:", self.cpu.alu.operation_count)
        print("Cycles:", self.cpu.cycles)
        print("----------------------------------------------------------------------------")



def main():
    cpu = CPU()
    view = View(cpu)
    controller = Controller(cpu, view)
    filename = sys.argv[1]
    controller.read_file(filename)
    controller.run_program()

if __name__ == "__main__":
    main()
else:
    print("program failed")