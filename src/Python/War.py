# File: War.py
# plays the war card game, using recursion when a war happens

from random import shuffle

def main():
    print("Welcome to Python War.")
    ans = input("For rules, type yes. To continue, type no. ")
    ans += " "
    if ans[0].lower() == "y":
        printRules()
    elif ans[0].lower() == "n":
        start()
    else:
        while ans[0].lower() != "y" or ans[0].lower() != "n":
            print("You did not enter a valid answer.")
            ans = input("For rules, type yes. To continue, type no. ")
            ans += " "
            if ans[0].lower() == "y":
                printRules()
            elif ans[0].lower() == "n":
                start()

def printRules():
    print("A deck of 52 cards is evenly cut between 2 players.")
    print("Each player holds their deck face down, and at the")
    print("same time flips over a card. The player who flipped")
    print("over the card with the higher face value wins both")
    print("cards and adds them to his deck. If both cards are")
    print("the same value, a war begins. Both players wager 3")
    print("cards face down, then flip a 4th card. The player")
    print("with the higher face value 4th card wins all cards")
    print("used in this round. If another war results, the")
    print("process repeats, with more cards wagered.")
    print("Ace is high,\ndeuce is low.\nPlay them right,\nand win the dough!")
    print("Good luck!\n\n")
    start()

def start():
    deck = ['Α♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', 'I0♥', 'J♥', 'Q♥', 'k♥', 'Α♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', 'I0♦', 'J♦', 'Q♦', 'k♦', 'Α♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', 'I0♣', 'J♣', 'Q♣', 'k♣', 'Α♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', 'I0♠', 'J♠', 'Q♠', 'k♠']
    shuffle(deck)
    
    lst_mycards = []
    lst_hiscards = []

    for i in range(0,52,2):
        lst_mycards.append(deck[i])

    for i in range(1,52,2):
        lst_hiscards.append(deck[i])

    while len(lst_mycards) >= 5 and len(lst_hiscards) >= 5:
        print("Your card:",lst_mycards[0],"\nOpponent's card:",lst_hiscards[0])
        if lst_mycards[0][0] > lst_hiscards[0][0]:
            lst_mycards.append(lst_hiscards.pop(0))
            lst_mycards.append(lst_mycards.pop(0))
            input("You won the round!\n")
        elif lst_mycards[0][0] < lst_hiscards[0][0]:
            lst_hiscards.append(lst_mycards.pop(0))
            lst_hiscards.append(lst_hiscards.pop(0))
            input("Your opponent won the round!\n")
        elif lst_mycards[0][0] == lst_hiscards[0][0]:
            war(lst_mycards, lst_hiscards, 1)
    if len(lst_mycards) < 5:
        input("You don't have enough cards to fulfill a war and have lost!\nGood game!\n")
    elif len(lst_hiscards) < 5:
        input("Your opponent doesn't have enough cards to fulfill a war and you have won!\nGood game!\n")


def war(lst_mycards, lst_hiscards, wars):
    input("It's a war!\n")
    print("Your card:",lst_mycards[4*wars],"\nOpponent's card:",lst_hiscards[4*wars])
    if lst_mycards[4*wars][0] > lst_hiscards[4*wars][0]:
        print("You won the war! You got:", sep=",", end="\n")
        for j in range(wars*5-(wars-1)):
            print(lst_mycards[0], sep=",", end=" ")
            lst_mycards.append(lst_mycards.pop(0))
            print(lst_hiscards[0], sep=",", end=" ")
            lst_mycards.append(lst_hiscards.pop(0))
        input("\n")
    elif lst_mycards[wars*4][0] < lst_hiscards[wars*4][0]:
        print("You lost the war! Your opponent got:", sep=",", end="\n")
        for j in range(wars*5-(wars-1)):
            print(lst_mycards[0], sep=",", end=" ")
            lst_hiscards.append(lst_mycards.pop(0))
            print(lst_hiscards[0], sep=",", end=" ")
            lst_hiscards.append(lst_hiscards.pop(0))
        input("\n")
    elif lst_mycards[wars*4][0] == lst_hiscards[wars*4][0]:
        war(lst_mycards, lst_hiscards, wars+1)


main()
