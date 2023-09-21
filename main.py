import sys

class article:
    isComplete = False
    description = ""
    taglist = []

    # for parsing existing plaintext article
    def __init__(self, ln):
        pass

    # For adding new articles
    def __init__(self, isComplete, description, taglist):
        self.isComplete = isComplete
        self.description = description
        self.duedate = duedate

def read_file(file):
    with open(file, 'r', encoding="utf-8") as f:
        return f.read()

if __name__ == '__main__':
    readlist=read_file(sys.argv[1])
    lines = readlist.split('\n')
    for line in lines:
        print(line)
