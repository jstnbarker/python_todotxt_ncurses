import sys

def read_file(file):
    with open(file, 'r', encoding="utf-8") as f:
        print(f.read())
        return f.read()

def parse():


if __name__ == '__main__':
    readlist=read_file(sys.argv[1])
    print(readlist)
