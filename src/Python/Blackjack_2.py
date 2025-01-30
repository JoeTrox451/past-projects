# Blackjack 2
# Simulates a game of blackjack with the player
# Upgrades from prev. version: better documentation, easier interface
# 2025 note: This version actually works, and works very well!
#  I'm pretty proud of it.

from random import randrange

def intro():
    print("Welcome to Python Blackjack.")
    ans = " "
    while ans[0].lower() != "y" or ans[0].lower() != "n":
        ans = input("For rules, type yes. To continue, type no. ")
        ans += " "
        if ans[0].lower() == "y":
            printRules()
        elif ans[0].lower() == "n":
            start()
        else:
            print("You did not enter a valid answer.")

def start():
    # main game function
    # deal first 2 cards to player and dealer
    ARY_PCards_num, ARY_DCards_num = First_Deal()
    # convert numbers to strings for printing
    ARY_PCards_name = stringify(ARY_PCards_num)
    ARY_DCards_name = stringify(ARY_DCards_num)
    # tell the player what cards are on the table
    stats(ARY_PCards_name, ARY_DCards_name)
    # convert the numbers to bj values for totaling
    ARY_PCards_value = bjeval(ARY_PCards_num)
    ARY_DCards_value = bjeval(ARY_DCards_num)
    INT_Ptotal = sum(ARY_PCards_value)
    INT_Dtotal = sum(ARY_DCards_value)
    # if the player gets 21 on the first draw, either win or draw
    if INT_Ptotal == 21 and INT_Dtotal != 21:
        instant_win(INT_Dtotal)
    if INT_Ptotal == 21 and INT_Dtotal == 21:
        instant_draw()
    # else, continue play normally
    while INT_Ptotal < 21 or INT_Dtotal < 21: # loop play until 21 is reached
        print("Your total is " + str(INT_Ptotal) + ".")
        STR_hitstay = input("Do you want to hit or stay?\n")
        STR_hitstay += " "
        if STR_hitstay[0].lower() == "h":
            # add a card to number list and re-evaluate the cards to print/total
            ARY_PCards_num.append(draw())
            ARY_PCards_name = stringify(ARY_PCards_num)
            ARY_PCards_value = bjeval(ARY_PCards_num)
            INT_Ptotal = sum(ARY_PCards_value)
            stats(ARY_PCards_name, ARY_DCards_name)
            if INT_Ptotal > 21:
                Ylose(INT_Ptotal)
            elif INT_Ptotal == 21 and INT_Dtotal != 21:
                instant_win(INT_Dtotal)
            elif INT_Ptotal == 21 and INT_Dtotal == 21:
                instant_draw()
        elif STR_hitstay[0].lower() == "s": # when player stays, it's the dealer's turn
            Dhitstay = "hit" # default to enter loop
            while Dhitstay == "hit":
                if INT_Dtotal < 17: # basic AI hits if total is lower than 17
                    ARY_DCards_num.append(draw())
                    ARY_DCards_name = stringify(ARY_DCards_num)
                    ARY_DCards_value = bjeval(ARY_DCards_num)
                    INT_Dtotal = sum(ARY_DCards_value)
                else: # if total is 17 or greater, dealer stays
                    Dhitstay = "stay"
            break
    showCards(ARY_PCards_name, ARY_DCards_name, INT_Ptotal, INT_Dtotal)

def printRules():
    # Prints the rules on the screen
    print("\nBlack Jack is a card game. The goal\nis to reach a numaric total of 21.\nYou loose if your total is more than 21.\nYou win if your total is higher than\nthe dealer's total. Face cards have a value\nof 10, Aces are 1 or 11, and all other cards\nare face value. This game has no bidding,\nit's just for fun. Blackjack is often played\nwith many decks shuffled together, so it is\npossible to have more than 4 of the same\nnumber dealt in a game.")
    print("\nYou and the dealer will be given two\ncards at the beginning, with only\none of the dealer's cards showing.\nYou can then either choose to hit (draw a card)\nor stay (don't draw a card). If you hit\nand your total goes over 21, you BUST and lose.\nIf your total is less than 21 and you stay,\nyour total is compared to the Dealer's total.\nIf yours is higher, you win. If not, you lose.\nIf they are the same, the game is a draw.")
    print("Good luck!")
    start()

def First_Deal():
    # create arrays for hands and adds 2 cards to each to start the game
    ARY_PCards_int = []
    ARY_DCards_int = []
    pc1 = draw()
    ARY_PCards_int.append(pc1)
    pc2 = draw()
    ARY_PCards_int.append(pc2)
    dc1 = draw()
    ARY_DCards_int.append(dc1)
    dc2 = draw()
    ARY_DCards_int.append(dc2)
    return ARY_PCards_int, ARY_DCards_int

def draw():
    # pick a random card from ace to king
    c = randrange(2,15)
    return c

def stringify(cards_int):
    # turn the list of numbers into names or str for the player to understand
    cards_str = []
    for i in cards_int:
        if i == 14:
            cards_str.append("Ace")
        elif i == 11:
            cards_str.append("Jack")
        elif i == 12:
            cards_str.append("Queen")
        elif i == 13:
            cards_str.append("King")
        else:
            cards_str.append(str(i))
    return cards_str

def stats(pc, dc):
    # tell the player what cards are on the table in a nice-looking format
    if len(pc) == 2: # first round, only 2 cards, no commas, simple.
        if pc[0] == "Ace" or pc[0] == "8":
            youhave = "\nYou have an "
        else:
            youhave = "\nYou have a "
        if pc[1] == "Ace" or pc[1] == "8":
            anda = " and an "
        else:
            anda = " and a "
        print(youhave + pc[0] + anda + pc[1] + ".")
        if dc[0] == "Ace" or dc[0] == "8":
            opphas = "The Dealer has an "
        else:
            opphas = "The Dealer has a "
        print(opphas + dc[0] + " showing.\n")
    else: # after first round, any number of cards can be in the hand
        print("\nYou have", end=" ")
        for p in range(0,len(pc)):
            if pc[p] == "Ace" or pc[p] == "8":
                youhave = "an"
            else:
                youhave = "a"
            if p < len(pc)-1:
                print(youhave, pc[p] + ",", end=" ")
            elif p == len(pc)-1:
                print("and", youhave, pc[p] + ".")
        if dc[0] == "Ace" or dc[0] == "8":
            opphas = "The Dealer has an "
        else:
            opphas = "The Dealer has a "
        print(opphas + dc[0] + " showing.\n")

def bjeval(card_num):
    # convert face cards to 10 and decide whether ace should be 1 or 11
    card_value = []
    for c in range(0,len(card_num)):
        if card_num[c] == 11 or card_num[c] == 12 or card_num[c] == 13:
            card_value.append(10)
        elif card_num[c] == 14:
            card_value.append(11)
        else:
            card_value.append(card_num[c])
    card_total = sum(card_value)
    while 11 in card_value and card_total > 21:
        card_value[card_value.index(11)] = 1
    return card_value

def showCards(pc, dc, pct, dct):
    print("Both you and The Dealer choose to stay")
    stats(pc, dc)
    if pct == dct:
        print("Your total is", str(pct) + ".")
        print("The Dealer's total is", str(dct) + ".")
        print("Both your totals are same.")
        print("The game is a draw.")
        print("Good game.")
        playAgain()
    elif pct == 21 and dct != 21:
        Ywin()
    elif pct == 21 and dct == 21:
        instant_draw()
    elif pct > 21:
        Ylose(pct)
    elif dct > 21:
        Close(pct, dct)
    elif max(pct, dct) == pct:
        print("Your total is", str(pct) + ".")
        print("The Dealer's total is", str(dct) + ".")
        print("You are closer to 21.")
        print("You have won!")
        print("Good game.")
        playAgain()
    elif max(pct, dct) == dct:
        print("Your total is", str(pct) + ".")
        print("The Dealer's total is", str(dct) + ".")
        print("The Dealer is closer to 21.")
        print("You have lost!")
        print("Good game.")
        playAgain()

def Ywin():
    print("Your total is 21! You have won!")
    print("Congratulations and good game.")
    playAgain()

def Ylose(pct):
    print("Your total is", str(pct) + ".")
    print("You have bust and lost!")
    print("Good game.")
    playAgain()

def Close(pct, dct):
    print("Your total is", str(pct) + ".")
    print("The Dealer's total is", str(dct) + ".")
    print("The Dealer has bust, but you have not!")
    print("You have won!")
    print("Good game.")
    playAgain()

def instant_win(INT_Dtotal):
    print("Your total is 21!")
    print("The Dealer's total is " + str(INT_Dtotal) + ".")
    print("CONGRATULATIONS!\nYou have won!")
    print("Good game.")
    playAgain()

def instant_draw():
    print("Your total is 21, but The Dealer's total is also 21.\nYou have tied The Dealer and the game is a draw.\nGood game.")
    playAgain()

def playAgain():
    c = input("\nDo you want to play again? ")
    c += " "
    if c[0].lower() == "y":
        start()
    else:
        print("Have a good evening!")
        input("Press <Enter> to quit.")
        quit()


if __name__ == "__main__": intro()
