"""
A simple blackjack simulation game.
Author: Ivan Lun Hui Chen
Date: 2023-04-23
"""
#function value is used to determine the value of the card given
def value(inCard):
    rank = inCard[0]
    value = 0
    secondary_value = 0
    if rank == 'A':
        value = 1
        secondary_value = 11
    elif rank == 'J' or rank == 'Q' or rank == 'K':
        value = 10
    else:
        rank = ''
        for x in inCard:
            if x.isalpha() == False:
                rank = rank + x
        if int(rank) in range(2,10):
            value = int(rank)
        elif rank == '10':
            value = 10
        else:
            value = 0
    return value,secondary_value


def output_score(hand):
    """
    Function that takes in a hand and returns the value(s) as a string
    """
    values = []
    for x in hand:
        values.append(value(x))

    result = 0
    secondary_result = 0
    outcome = ""
    countA = 0
    for y in range(len(values)):
        result = result + values[y][0]
        if values[y][-1] == 11:
            countA += 1
    if countA >= 1:
        secondary_result = result + 10
    if result == 21 or secondary_result == 21:
        if len(hand) == 2:
            outcome = "Blackjack!"
        else:
            outcome = "21"
    elif result < 21 and secondary_result == 0:
        outcome = str(result)
    elif result > 21:
        outcome = "Bust!"
    elif secondary_result > 21:
        outcome = str(result)
    else:
        outcome = str(result) + " or " + str(secondary_result)
    return outcome

def is_blackjack(hand):
    """
    Whether the hand represents a Blackjack hand. Return True if it is blackjack, False otherwise
    """
    if output_score(hand) == "Blackjack!":
        return True
    else:
        return False

def is_bust(hand):
    """
    Whether the hand is bust (exceeds 21). Return True if it is bust, False otherwise
    """
    if output_score(hand) == "Bust!":
        return True
    else:
        return False

def get_advice(player_hand, dealer_hand):
    """
    Computes a suggestion as to the action to take given the cards. Return either 'Hit' or 'Stand'
    """    
    outcome = output_score(player_hand)
    dealerValue = value(dealer_hand)
    advice = ""

    if "or" in str(outcome):
        possibilities = list(outcome.split("or"))
        possibility2 = int(possibilities[1])
        if (possibility2 == 18 and dealerValue[0] in range(2,9)) or possibility2 >=19:
            advice = "Stand"
        else:
            advice = "Hit"
    else:
        if (int(outcome) == 12 and dealerValue[0] in range(4,7)) or (int(outcome) in range(13,17) and dealerValue[0] in range(2,7)) or int(outcome) >=17:
            advice = "Stand"
        else:
            advice = "Hit"
    return advice


def get_high_score(hand):
    """
     Returns the maximum (non-bust) value of the hand. If the hand contains an ace,
     this means the higher of the two values is picked, provided it does not exceed 21.
    """
    outcome = output_score(hand)
    maximum = 0
    if outcome == "Blackjack!":
        maximum = 21
    elif "or" in outcome:
        possibilities = list(outcome.split("or"))
        maximum = int(possibilities[1])
    else:
        maximum = int(outcome)
    return maximum
    

def get_winner(player_hand, dealer_hand):
    """
    Given the player's hand and the dealer's hand, return a string signifying who won (or whether it's a push)
    """
    playerOutcome = output_score(player_hand)
    dealerOutcome = output_score(dealer_hand)

    if "or" in str(playerOutcome):
        possibilities = list(playerOutcome.split("or"))
        playerOutcome = int(possibilities[1])
    if "or" in str(dealerOutcome):
        possibilities = list(dealerOutcome.split("or"))
        dealerOutcome = int(possibilities[1])
    gameOutcome = ""
    if playerOutcome == "Blackjack!":
        gameOutcome = "Player wins!"
    elif playerOutcome == "Bust!":
        gameOutcome = "Dealer wins!"
    elif dealerOutcome == "Blackjack!":
        gameOutcome = "Dealer wins!"
    elif dealerOutcome == "Bust!":
        gameOutcome = "Player wins!"
    elif int(playerOutcome) > int(dealerOutcome):
        gameOutcome = "Player wins!"
    elif int(playerOutcome) < int(dealerOutcome):
        gameOutcome = "Dealer wins!"
    else:
        gameOutcome = "Push!"
    return gameOutcome    


"""
Do not modify any code below this comment! This section is completed by Steve James.
Author: Steve James <steven.james@wits.ac.za>
"""

import random


class Deck:

    def __init__(self):
        self._cards = list()
        self._rng = random.Random(42)
        self.reset()

    def _rank_to_string(self, rank):
        special = {
            1: 'A',
            11: 'J',
            12: 'Q',
            13: 'K'
        }
        return special.get(rank, str(rank))

    def reset(self):
        self._cards.clear()
        for rank in range(1, 14):
            r = self._rank_to_string(rank)
            for suit in ['h', 'c', 's', 'd']:
                self._cards.append(r + suit)
        self._rng.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()



def get_input(message, legal_options):
    while True:
        print(message, end='')
        option = input()
        if len(option) == 0:
            continue
        option = option[0].upper()
        if option in legal_options:
            return option
        else:
            print("Invalid input '{}'".format(option))


def hand_to_string(hand):
    return '{} -> {}'.format(
        ' '.join(hand),
        output_score(hand)
    )


def play_round(deck):
    player_hand = list()
    dealer_hand = list()
    deck.reset()

    dealer_hand.append(deck.draw())
    player_hand.append(deck.draw())
    player_hand.append(deck.draw())

    print('Dealer shows {}'.format(hand_to_string(dealer_hand)))
    print('Player shows {}'.format(hand_to_string(player_hand)))
    if is_blackjack(player_hand):
        print('Player wins!')
        return

    # Player's turn
    playing = True
    while playing and not is_bust(player_hand):
        action = get_input('(H)it, (S)tand, or (A)dvice? ', {'H', 'S', 'A'})
        if action == 'H':
            player_hand.append(deck.draw())
            print('Player shows {}'.format(hand_to_string(player_hand)))
        elif action == 'S':
            playing = False
        else:
            print('Advice: {}'.format(get_advice(player_hand, dealer_hand[0])))

    if playing:
        # player must be bust
        print('Dealer wins!')
        return

    # dealer's turn
    while not is_bust(dealer_hand) and get_high_score(dealer_hand) < 17:
        dealer_hand.append(deck.draw())
        print('Dealer shows {}'.format(hand_to_string(dealer_hand)))

    print(get_winner(player_hand, dealer_hand))


if __name__ == '__main__':

    running = True
    deck = Deck()
    while running:
        option = get_input('(N)ew round or (Q)uit? ', {'N', 'Q'})
        if option == 'N':
            play_round(deck)
            print('******************************************')
        elif option == 'Q':
            running = False
