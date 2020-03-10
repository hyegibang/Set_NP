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
