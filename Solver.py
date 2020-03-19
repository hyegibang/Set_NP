import random
class deck:
    def __init__(self):
        self.cards=[]
        self.table=[]
    def add_cards(self):
        cards = []
        for i in ("green","purple","red"):
            for j in ("oval","diamond","squiggle"):
                for k in ("1","2","3"):
                    for l in ("solid","stripped","outline"):
                        self.cards.append(card(i,j,k,l))
        #return cards

    def make_table(self):
        for i in range (0,11):
            y=random.choice(self.cards)
            self.table.append(y)

class card:
    def __init__(self,color,shape,shade,number):
        self.color=color
        self.shape=shape
        self.shade=shade
        self.number=number

def matches(table):
    matches = []
    for i in range(len(table)):
        for j in range(1,len(table)):
            for k in range(2,len(table)):
                A = isCardMatch(table[i],table[j],table[k])
                if A:
                    matches.append([table[i],table[j],table[k]])
    return matches

def isCardMatch(c1,c2,c3):
    if c1.color == c2.color == c3.color:
        return True
    elif c1.color != c2.color != c3.color:
        return True
    elif c1.shape == c2.shape == c3.shape:
        return True
    elif c1.shape != c2.shape != c3.shape:
        return True
    elif c1.number == c2.number == c3.number:
        return True
    elif c1.number != c2.number != c3.number:
        return True
    elif c1.shape == c2.shape == c3.shape:
        return True
    elif c1.shape != c2.shape != c3.shape:
        return True
    else:
        return False






if __name__ == '__main__':
    deckCard = deck()
    deckCard.add_cards()
    deckCard.make_table()
    match_list = matches(deckCard.table)
