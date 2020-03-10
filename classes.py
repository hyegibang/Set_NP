import random
class deck:
    def __init__(self):
        self.cards=[]
        self.table=[]
    def add_cards(self):
        for i in ("green","purple","red"):
            for j in ("oval","diamond","squiggle"):
                for k in ("1","2","3"):
                    for l in ("solid","stripped","outline"):
                        self.cards.append(card(i,j,k,l))

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
x=deck()
x.add_cards()
x.make_table()
print(x.table)
