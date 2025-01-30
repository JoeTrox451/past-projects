# blackjack.py
# Simulates a game of blackjack between the program and the user.
# 2025 note: This version is a very basic version that only kind of works.
#  It was made for Python version 2, so it won't even run.
#  Comparing it to Blackjack_2 shows how much I learned since then.

from random import randrange
from string import lower

def main():
    print "This program plays a game of blackjack with the user."
    ans = raw_input("For rules, type yes. To continue, type no. ")
    if lower(ans[0]) == "y":
        printRules()
    pc, cc = deal()
    pc.append(0)
    cc.append(0)
    stats(pc, cc)
    pct = 0
    cct = 0
    pcon = "stay"
    c = "stay"
    pct = pevalCards(pc)
    cct = cevalCards(cc, cct, c)
    while pct < 21 or cct < 21:
        c = checkStats(pct, cct)
        print "\nYour total is", pct
        pcon = raw_input("Do you want to hit or stay? ")
        if lower(pcon[0]) == "h":
            if pc[2] == 0:
                pc[2] = shuffle()
            else:
                pc.append(shuffle())
        elif lower(pcon[0]) == "s":
            if c == "hit":
                if cc[2] == 0:
                    cc[2] = shuffle()
                else:
                    cc.append(shuffle())
                if lower(pcon[0]) == "s" and (c == "stay"):
                    showCards(pc, cc, pct, cct)
        pct = pevalCards(pc)
        cct = cevalCards(cc, cct, c)
        if lower(pcon[0]) == "s" and (c == "stay"):
            showCards(pc, cc, pct, cct)
        pc, cc = evalFaceLoop(pc, cc)
        stats(pc, cc)
    checkStats(pct, cct)


def printRules():
    print "\nBlack Jack is a card game. The goal is\nto reach a numaric total of 21. You\nloose if your total is more than 21.\nFace cards have a value of 10, Aces\nare 1 or 11 (you choose), and all other cards are face value.\nThere is no bidding in this version of the game."
    print "Good luck!"

def deal():
    pc = []
    cc = []
    pc1 = shuffle()
    pc.append(pc1)
    pc2 = shuffle()
    pc.append(pc2)
    cc1 = shuffle()
    cc.append(cc1)
    cc2 = shuffle()
    cc.append(cc2)
    return pc, cc

def shuffle():
    c = randrange(1,14)
    c = evalFace(c)
    return c

def evalFaceLoop(pc, cc):
    for i in range(len(pc)):
        pc[i] = evalFace(pc[i])
    for i in range(len(cc)):
        cc[i] = evalFace(cc[i])
    return pc, cc

def evalFace(c):
    if c == 11:
        c = "Jack"
    elif c == 12:
        c = "Queen"
    elif c == 13:
        c = "King"
    elif c == 1:
        c = "Ace"
    return c

def stats(pc, cc):
    if pc[2] == 0:
        print "\nYou have a", pc[0], "and a", pc[1], "."
        print "Your opponent has a", cc[1], "showing."
    else:
        print "\nYou have",
        for p in pc:
            if p != pc[len(pc)-1]:
                print ", a", p, 
            elif p == pc[len(pc)-1]:
                print ", and a", str(p) + "."
        print "Your opponent has a", cc[1], "showing."
        
        
def checkStats(pct, cct):
    if pct > 21:
        Yloose(pct)
    elif pct == 21:
        Ywin()
    else:
        if cct == 21:
            Cwin(pct, cct)
        elif cct > 21:
            Cloose(pct, cct)
        elif cct < 21:
            d = 21 - cct
            if d <= 5:
                c = "stay"
            else:
                c = "hit"
    return c

def pevalCards(pc):
    pct = 0
    for p in range(len(pc)):
        pc[p] = analCards(pc[p])
    for m in range(len(pc)):
        pct = pct + pc[m]
    return pct

def analCards(c):
    if c == "Jack":
        c = 10
    elif c == "Queen":
        c = 10
    elif c == "King":
        c = 10
    elif c == "Ace":
        print "\nYou have an Ace."
        c = input("Do you want your Ace to be a 1 or 11? ")
    else:
        c = c
    return c

def cevalCards(cc, ct, c):
    cc[0] = canalCards(cc[0], 0)
    cc[1] = canalCards(cc[1], cc[0])
    st = cc[0] + cc[1]
    cc[2] = canalCards(cc[2], st)
    if c == "hit":
        for i in range(len(cc)):
            ct = ct + cc[i]
    return ct

def canalCards(c, st):
    if c == "Jack" or c == "Queen" or c == "King":
        c = 10
    elif c == "Ace":
        c = cevalAce(c, st)
    else:
        c = c
    return c

def cevalAce(a, st):
    d = 21 - st
    if d <= 10:
        a = 11
    else:
        a = 1
    return a

def Ywin():
    print "Your total is 21! You have won!"
    print "Congradulations and good game."
    playAgain()

def Yloose(pct):
    print "Your total is", pct
    print "You have lost!"
    print "Good game."
    playAgain()

def Cwin(pct, cct):
    print "Your total is", pct
    print "Your opponent's total is", cct
    print "Your opponent has won!"
    print "Good game."
    playAgain()

def Cloose(pct, cct):
    print "Your total is", pct
    print "Your opponent's total is", cct
    print "You have won!"
    playAgain()

def playAgain():
    c = raw_input("Do you want to play again? ")
    if c[0] == "y" or c[0] == "Y":
        main()
    else:
        print "Goodbye."
        raw_input("Press <Enter> to quit.")
        quit()

def showCards(pc, cc, pct, cct):
    print "Both you and your opponent choose to stay"
    if pc[2] == 0:    
        print "You have a", pc[0], "and a", pc[1], "."
    else:
        print "\nYou have", 
        for p in pc:
            if p != pc[len(pc)-1]:
                print ", a", p, 
            elif p == pc[len(pc)-1]:
                print ", and a", str(p) + "."
    if cc[2] == 0:
        print "Your opponent has", cc[0], "and a", cc[1], "."
    else:
        print "Your opponent has", 
        for c in cc:
            if c != cc[len(cc)-1]:
                print ", a", c, 
            elif c == cc[len(cc)-1]:
                print ", and a", str(c) + "."
    if pct == cct:
        print "Your total is", pct, "."
        print "Your opponent's total is", cct, "."
        print "Both your totals are same."
        print "The game is a draw"
        print "Good game"
        playAgain()
    elif max(pct, cct) == pct:
        print "Your total is", pct, "."
        print "Your opponent's total is", cct, "."
        print "You are closer to 21."
        print "You have won!"
        print "Good game"
        playAgain()
    elif max(pct, cct) == cct:
        print "Your total is", pct, "."
        print "Your opponent's total is", cct, "."
        print "Your opponent is closer to 21."
        print "You have lost!"
        print "Good game"
        playAgain()
        


if __name__ == '__main__': main()
