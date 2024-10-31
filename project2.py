import sys

def readInFile(filename):
    in_file = open(filename, "rb")
    op = in_file.read(6)
    print(op)

def main():
    filename = sys.argv[1]
    readInFile(filename)

if __name__ == "__main__":
    main()
else:
    print("program failed")