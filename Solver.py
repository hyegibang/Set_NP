from classes import *
import sys

def Solve(table, matches, id=0):

    #Base Cases
    if(len(table)==0):
        return True
    if(len(matches)==0):
        return False

    print("Table ****** " + str(id))
    for v in table:
        v.print_card()

    #Take off one match
    firstMatch = matches[0]
    matches = updateMatches(matches, firstMatch)
    tableRemoved = updateTable(table, firstMatch)

    id+=1
    #Try either using the match or not using it
    solutionA = Solve(tableRemoved, matches, id)
    solutionB = Solve(table, matches, id)

    if(solutionA or solutionB):
        return True
    else:
        return False

def updateTable(table, match):
    newTable = []
    idsToRemove = []
    for card in match:
        idsToRemove.append(card.id)
    for card in table:
        if(not card.id in idsToRemove):
            newTable.append(card)
    return newTable

def hasMatchingCards(m1, m2):
    for c1 in m1:
        for c2 in m2:
            if(c1.id == c2.id):
                return True
    return False

def updateMatches(matches, match):
    newMatches = []
    for rawMatch in matches:
        if(not hasMatchingCards(rawMatch, match)):
            newMatches.append(rawMatch)
    return newMatches


def matches(table):
    matches = []
    for i in range(len(table)):
        for j in range(1,len(table)):
            for k in range(2,len(table)):
                if(i!=j and i!=k and j!=k):
                    if isCardMatch(table[i],table[j],table[k]):
                        matches.append([table[i],table[j],table[k]])
    return matches

def isCardMatch(c1,c2,c3):
    """
    Takes in three card objects, return a boolean value

    Returns True if all three cards "Match" along all four dimensions (color, number, shape, shade)
    Return False if any of the dimensions of the three cards do not match

    A card is "Matched" if all three cards are either all the same or all unique
    """
    colorMatched = False
    numberMatched = False
    shapeMatched = False
    shadeMatched = False

    #If all the colors are the same or all arent the same, colors are Matched
    if c1.color == c2.color == c3.color:
        colorMatched = True
    if (c1.color != c2.color) and (c1.color != c3.color) and (c2.color != c3.color):
        colorMatched = True

    #If all the numbers are the same or all arent the same, numbers are Matched
    if c1.number == c2.number == c3.number:
        numberMatched = True
    if (c1.number != c2.number) and (c1.number != c3.number) and (c2.number != c3.number):
        numberMatched = True

    #If all the shape are the same or all arent the same, shape are Matched
    if c1.shape == c2.shape == c3.shape:
        shapeMatched = True
    if (c1.shape != c2.shape) and (c1.shape != c3.shape) and (c2.shape != c3.shape):
        shapeMatched = True

    #If all the shade are the same or all arent the same, shade are Matched
    if c1.shade == c2.shade == c3.shade:
        shadeMatched = True
    if (c1.shade != c2.shade) and (c1.shade != c3.shade) and (c2.shade != c3.shade):
        shadeMatched = True

    #If all are dimensions match, then this is a match
    if( colorMatched and numberMatched and shapeMatched and shadeMatched):
        return True
    else:
        return False

if __name__ == '__main__':
    x=deck()
    x.add_cards()
    if(len(sys.argv) > 1):
        testFile = sys.argv[1]
        x.makeTableFromFile(testFile)
    else:
        x.make_default_table()
    print("Deck Created and Table Set")
    matches = matches(x.table)
    solveable = Solve(x.table, matches)
    print("Finished! The table is " + str(solveable))
