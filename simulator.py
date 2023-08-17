from itertools import product
import random

def convertCardToNumber(face):
    if face == "Ace":
        return 14
    if face == "King":
        return 13
    elif face == "Queen":
        return 12
    elif face == "Jack":
        return 11
    else:
        return int(face)

def playWar():
    faces = list(range(2,11)) + ["King","Queen","Jack","Ace"]
    colour = ["Spades", "Hearts", "Clubs", "Diamonds"]
    deck = ["{} of {}".format(*card) for card in product(faces, colour)]
    random.shuffle(deck)
    hand1 = deck[:26]
    hand2 = deck[26:]
    player1_wins = []
    player2_wins = []
    numTurns = 0

    while len(hand1) < 52 and len(hand2) < 52 and numTurns < 5000:
        numTurns += 1
        # print("---")
        # print("Turn number {}".format(numTurns))
        while len(hand1) > 0 and len(hand2) > 0:
            card1 = hand1.pop(0)
            card2 = hand2.pop(0)
            # print("Player 1: {} \t Player 2: {}".format(card1, card2))

            if convertCardToNumber(card1.split()[0]) > convertCardToNumber(card2.split()[0]):
                # print("Player 1 wins!")
                player1_wins.append(card1)
                player1_wins.append(card2)
            elif convertCardToNumber(card1.split()[0]) < convertCardToNumber(card2.split()[0]):
                # print("Player 2 wins!")
                player2_wins.append(card1)
                player2_wins.append(card2)
            else:
                # print("It's war! Card1: {}, Card2: {}".format(card1, card2))
                cards1 = []
                cards2 = []
                winner = False
                while not winner:
                    if len(hand1) > 1 and len(hand2) > 1:
                        cards1.append(hand1.pop(0))
                        cards1.append(hand1.pop(0))
                        cards2.append(hand2.pop(0))
                        cards2.append(hand2.pop(0))
                        if convertCardToNumber(cards1[-1].split()[0]) > convertCardToNumber(cards2[-1].split()[0]):
                            # print("Player 1 wins the war!")
                            winner = True
                            player1_wins.append(card1)
                            player1_wins.append(card2)
                            for card in cards1:
                                player1_wins.append(card)
                            for card in cards2:
                                player1_wins.append(card)
                        elif convertCardToNumber(cards1[-1].split()[0]) < convertCardToNumber(cards2[-1].split()[0]):
                            # print("Player 2 wins the war!")
                            winner = True
                            player2_wins.append(card1)
                            player2_wins.append(card2)
                            for card in cards1:
                                player2_wins.append(card)
                            for card in cards2:
                                player2_wins.append(card)
                        else:
                            # print("War is a tie, running war again...")
                            pass
                    else:
                        # print("players don't have enough cards for war. Returning cards to each player.")
                        winner = True
                        player1_wins.append(card1)
                        player2_wins.append(card2)
                        for card in cards1:
                            player1_wins.append(card)
                        for card in cards2:
                            player2_wins.append(card)

        for card in player1_wins:
            hand1.append(card)
        for card in player2_wins:
            hand2.append(card)
        random.shuffle(hand1)
        random.shuffle(hand2)
        player1_wins = []
        player2_wins = []
        # print("Player 1: {} \t Player 2: {}".format(len(hand1), len(hand2)))

    print("Number of rounds: {}".format(numTurns))
    print("Winner: Player {}".format(1 if len(hand1) > len(hand2) else 2))
    return numTurns

def main():
    turnsPerGame = []
    total = 0
    for i in range(10000):
        turns = playWar()
        turnsPerGame.append(turns)
        total += turns
    average = total / len(turnsPerGame) 
    print("Turns per game: {}".format(turnsPerGame))
    print("Average number of turns: {}".format(average))
    print("Max turns: {}".format(max(turnsPerGame)))
    print("Min turns: {}".format(min(turnsPerGame)))

if __name__ == "__main__":
    main()