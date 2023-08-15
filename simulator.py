from itertools import product
import random

def main():
    # generate the deck
    faces = list(range(2,11)) + ["King","Queen","Jack","Ace"]
    # print(faces)
    colour = ["Spades", "Hearts", "Clubs", "Diamonds"]
    deck = ["{} of {}".format(*card) for card in product(faces, colour)]
    # print("There are {} cards in a deck".format(len(faces)*len(colour)))
    # print("The cards are: {}".format(deck))

    # randomize the deck
    random.shuffle(deck)

    hand1 = deck[:26]
    hand2 = deck[26:]
    # print(len(hand1), len(hand2))

    player1_wins = []
    player2_wins = []

    i = 0
    while len(hand1) < 52 and len(hand2) < 52:
        i += 1
        while len(hand1) > 0 and len(hand2) > 0:
            card1 = hand1.pop()
            card2 = hand2.pop()
            # print("Player 1: {} \t Player 2: {}".format(card1, card2))

            if card1.split()[0] > card2.split()[0]:
                # print("Player 1 wins!")
                player1_wins.append(card1)
                player1_wins.append(card2)
            elif card1.split()[0] < card2.split()[0]:
                # print("Player 2 wins!")
                player2_wins.append(card1)
                player2_wins.append(card2)
            else:
                print("It's a tie!", card1, card2, len(hand1), len(hand2))
                cards1 = []
                cards2 = []
                if len(hand1) > 1 and len(hand2) > 1:
                    cards1.append(hand1.pop())
                    cards1.append(hand1.pop())
                    cards2.append(hand2.pop())
                    cards2.append(hand2.pop())
                    if cards1[-1].split()[0] > cards2[-1].split()[0]:
                        player1_wins.append(card1)
                        player1_wins.append(card2)
                        for card in cards1:
                            player1_wins.append(card)
                        for card in cards2:
                            player1_wins.append(card)
                    elif cards1[-1].split()[0] < cards2[-1].split()[0]:
                        player2_wins.append(card1)
                        player2_wins.append(card2)
                        for card in cards1:
                            player2_wins.append(card)
                        for card in cards2:
                            player2_wins.append(card)
                    else:
                        player1_wins.append(card1)
                        player2_wins.append(card2)
                        for card in cards1:
                            player1_wins.append(card)
                        for card in cards2:
                            player2_wins.append(card)
                else:
                    player1_wins.append(card1)
                    player2_wins.append(card2)
                # hand1.insert(0,card1)
                # hand2.insert(0,card2)
        for card in player1_wins:
            hand1.append(card)
        for card in player2_wins:
            hand2.append(card)
        random.shuffle(hand1)
        random.shuffle(hand2)
        player1_wins = []
        player2_wins = []
        print("Player 1: {} \t Player 2: {}".format(len(hand1), len(hand2)))
    print("Number of rounds: {}".format(i))

if __name__ == "__main__":
    main()