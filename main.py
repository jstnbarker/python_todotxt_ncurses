import sys

class todolist:
    pass

class article:
    isComplete = False
    description = ""
    taglist = []
    duedate = "1970-01-01"

    # for parsing existing plaintext articles
    def __init__(self, ln):
        raw = ln.split()

        if(raw[0] == "x"):
            raw.pop(0)
            self.isComplete=True

        while(len(raw) != 0):
            current=raw[0] 
            flag=current[0]

            # Check if current item is a tag
            if(flag == "+"):
                current.replace("","+")
                self.taglist.append(current)
                pass

            elif(current[0:4:1] == "due:"):
                print(current[3:])
                self.duedate=current[3:]

            # Current item has no flag, must be part of description
            else: 
                self.description+=raw[0]

            raw.pop(0)

        print(self.isComplete, self.description, self.taglist)

def read_file(file):
    with open(file, 'r', encoding="utf-8") as f:
        return f.read()

if __name__ == '__main__':
    readlist=read_file(sys.argv[1])
    lines = readlist.splitlines()

    
    for line in lines:
        print(line)
        item = article(line)
