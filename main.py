import sys
import curses
from curses import wrapper 

class todolist:
    pass

class article_obj:
    isComplete = False
    description = ""
    taglist = []
    duedate = "1970-01-01"
    context = ""

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
                self.taglist.append(current.replace("+",""))
            elif(flag == "@"):
                current=current.replace("@","")
                self.context=current
            elif(current[0:4:1] == "due:"):
                self.duedate=current[4:]
            # Current item has no flag, must be part of description
            else: 
                self.description+=raw[0]+" "
            raw.pop(0)

    def __str__(self):
        return f"{self.isComplete}, {self.description}, {self.context}, {self.taglist}, {self.duedate}"

    def complete(self):
        self.isComplete = not self.isComplete

    def getDescription():
        return self.description
    
    def getDue():
        return self.duedate
    
    def getContext():
        return self.context

    def getTaglist():
        return self.taglist


def read_file(file):
    with open(file, 'r', encoding="utf-8") as f:
        return f.read()

def display_list(stdscr, selected_row):
    stdscr.clear()

    width=curses.COLS-1
    completion = curses.newwin(40, 2, 1, 0)
    completion.clear()

    for i, article in enumerate(article_list):
        x = 1
        y = i + 1


        mark = " "
        if(article.isComplete):
            mark="x"

        if i == selected_row:
            completion.attron(curses.A_REVERSE)
            completion.addstr(y, x, mark)
            completion.attroff(curses.A_REVERSE)
        else:
            completion.addstr(y,x,mark)

def home(stdscr):
    stdscr.clear()
    stdscr.refresh()
    stdscr.getkey()

    stdscr.nodelay(1)

    current_row = 0
    display_list(stdscr, current_row)
    while True:
        c = stdscr.getch()
        if c == ord('q'):
            break
        elif c == ord('j'):
            current_row+=1
            display_list(stdscr, current_row)
        elif c == ord('k') and current_row < len(article_list):
            current_row-=1
            display_list(stdscr, current_row)
        elif c == ord('x'):
            article_list[current_row].complete()
            display_list(stdscr, current_row)

if __name__ == '__main__':
    readlist=read_file(sys.argv[1])
    lines = readlist.splitlines()

    article_list = []
    for line in lines:
        article = article_obj(line)
        article_list.append(article)

    wrapper(home)
