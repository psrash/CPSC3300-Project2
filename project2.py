import sys

class Model:
    def __init__(self, instruction):
        self.instruction = instruction

def readRType(instruction):
    #get operand
    op = (instruction >> 26) & 0b111111
    rs_register = (instruction >> 21) & 0b11111

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

    rs_register = (instruction >> 21) & 0b11111
    print(f"The rs register is: {rs_register:05b}")

def main():
    filename = sys.argv[1]
    readInFile(filename)

if __name__ == "__main__":
    main()
else:
    print("program failed")