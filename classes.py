import random
from Solver import *

class deck:
    """
    Creates a deck of card, a total of 81 cards. With the deck of cards, it randomly
    selects 12 cards and puts them in a table
    """
    def __init__(self):
        self.cards=[]
        self.table=[]
    def add_cards(self):
        id=0
        for i in ("green","purple","red"):
            for j in ("oval","diamond","squiggle"):
                for l in ("solid","stripped","outline"):
                    for k in ("1","2","3"):
                        self.cards.append(card(i,j,l,k,id))
                        id+=1

    def make_default_table(self):
        for i in range (0,12):
            y=random.choice(self.cards)
            self.table.append(y)

    def makeTableFromFile(self, testFile):
        f = open(testFile, "r")
        lines = [line.split() for line in f.readlines()]
        f.close()

        cards = []

        lines = lines[1:]
        idVal = 0
        for line in lines:
            if(len(line)):
                if(line[0] == 'p'):
                    self.numCards= line[1]
                if(line[0] not in ('c', 'p') ):
                    color = line[0]
                    shape = line[1]
                    shade = line[2]
                    number = line[3]
                    id = idVal
                    idVal+=1
                    self.table.append(card(color,shape,shade,number,id))
        return


class card:
    """
    Every Card has four different property: color, shape, shade, and quantity.
    """
    def __init__(self,color,shape,shade,number,id):
        self.color=color
        self.shape=shape
        self.shade=shade
        self.number=number
        self.id = id

    def print_card(self):
        print(str(self.id) + " *** " + self.color + " " + self.shape + " " + self.shade + " " + self.number )

if __name__ == '__main__':
    filename = sys.argv[1]
    x=deck()
    x.add_cards()
    if(len(filename) == 0):
        x.make_default_table()
    matches = matches(x.table)
    for m in matches:
        for x in m:
            x.print_card()
    print("Deck Created and Table Set")
