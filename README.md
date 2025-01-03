# simple_blackjack
This is a simplified implementation of blackjack using python.

# rules
 The value of a person’s hand is calculated as the sum of the individual cards: aces count as either
 1 or 11, tens and face cards (kings, queens and jacks) are worth 10 points, while the remaining
 cards are scored according to their face value.
 The rules of this version mirror standard Blackjack, but the player only has two actions available to him: hit or
 stand.\
 Scoring is slightly more involved when a hand contains an ace. In this case there are two
 possible values, since an ace can be treated as either 1 or 11. If both possible values do not
 exceed 21, then the hand is said to contain a usable ace. If the larger of the values is more than
 21, then only the lower value is considered. For example, a hand consisting of an ace and a six
 has a value of either 7 or 17, while a hand consisting of an ace, a six and a ten has a value of 17
 only.\
 A special case occurs when the first two cards of either contestant add up to 21. In such a
 case, the person is said to have Blackjack and immediately win the round. A hand with more
 than two cards that add up to 21 is not Blackjack.

# play
At the beginning of the round, the dealer receives one card while the player receives two. First,
 we examine the player’s cards. If they add up to 21, the player has Blackjack and immediately
 wins the round. Otherwise the player is given two options: to request another card (hit) or
 to stick with his current hand (stand). The player keeps making decisions until he chooses to
 stand, or the value of his hand exceeds 21. If his hand exceeds 21, he is said to have busted, and
 the dealer wins the round.\
 If the player completes his turn without busting, the dealer then takes his turn. The dealer
 first draws a card. If this results in the dealer achieving Blackjack, then he immediately wins the
 round. Otherwise, the dealer keeps drawing cards until the value of his hand is greater than 16,
 at which point he stops drawing cards. If the dealer has a usable ace, then he stops if his higher
 score is greater than 16.\
 If the dealer busts, or has a value less than that of the player, then the player wins. If the
 dealer has a higher value, the player loses. And if both have the same value, they tie (push).

# input
 A card is represented as a string in the form (rank)(suit). (rank) is either 2-10, J (jack), Q (queen), K (king), or A (ace),
 while (suit) is either c (clubs), d (diamonds), h (hearts), or s (spades).
 For example, the “ten of hearts” is represented by 10h, while the “ace of clubs” is Ac.

# advice option
This is an additional option in which the player receives an advice based on the table below\
If the player has a usable ace\
 Player's current value is on the left most column and the Dealer’s Card spans the following columns with the values 2 3 4 5 6 7 8 9 10 A\
 12 Hit Hit Hit Hit Hit Hit Hit Hit Hit Hit\
 13 Hit Hit Hit Hit Hit Hit Hit Hit Hit Hit\
 14 Hit Hit Hit Hit Hit Hit Hit Hit Hit Hit\
 15 Hit Hit Hit Hit Hit Hit Hit Hit Hit Hit\
 16 Hit Hit Hit Hit Hit Hit Hit Hit Hit Hit\
 17 Hit Hit Hit Hit Hit Hit Hit Hit Hit Hit\
 18 Stand Stand Stand Stand Stand Stand Stand Hit Hit Hit\
 19+ Stand Stand Stand Stand Stand Stand Stand Stand Stand Stand\
 If the player does not have a usable ace\
 4-8 Hit Hit Hit Hit Hit Hit Hit Hit Hit Hit\
 9 Hit Hit Hit Hit Hit Hit Hit Hit Hit Hit\
 10 Hit Hit Hit Hit Hit Hit Hit Hit Hit Hit\
 11 Hit Hit Hit Hit Hit Hit Hit Hit Hit Hit\
 12 Hit Hit Stand Stand Stand Hit Hit Hit Hit Hit\
 13 Stand Stand Stand Stand Stand Hit Hit Hit Hit Hit\
 14 Stand Stand Stand Stand Stand Hit Hit Hit Hit Hit\
 15 Stand Stand Stand Stand Stand Hit Hit Hit Hit Hit\
 16 Stand Stand Stand Stand Stand Hit Hit Hit Hit Hit\
 17+ Stand Stand Stand Stand Stand Stand Stand Stand Stand Stand\

 # output
 The program will print out the winner if there is one, Push! if draw.