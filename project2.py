import sys

class Model:
    def __init__(self, instruction):
        self.instruction = instruction

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