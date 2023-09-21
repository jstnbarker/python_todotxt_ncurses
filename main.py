import sys

class article:
    isComplete = False
    description = ""
    taglist = []

    def __init__(self, isComplete, description, taglist, duedate):
        self.isComplete = isComplete
        self.description = description
        self.duedate = duedate

def read_file(file):
    with open(file, 'r', encoding="utf-8") as f:
        print(f.read())
        return f.read()

if __name__ == '__main__':
    readlist=read_file(sys.argv[1])
    print(readlist)
