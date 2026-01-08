'''
Docstring for war.war
'''

import random

# Global variables for storing card suits, ranks, and dictionary for converting ranks to ints for comparison
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

# Card Class storing individual card suits and ranks
class Cards:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

# Deck Class for storing 52 Card objects representing a standard deck of cards. Initially unshuffled upon
# instantiation. 
class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Cards(suit, rank)
                self.all_cards.append(created_card)
    
    # Method for shuffling deck utilizing random module
    def shuffle(self):
        random.shuffle(self.all_cards)
  
    # Method for dealing singlue card to player(s)
    def deal_one(self):
        return self.all_cards.pop()

# Player Class for storing name of players and the status of their hands at any given point.  
class Player():
    
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    # Method for removing the top card from a player's hand, simulating placing a card down on the table
    def remove_one(self):
        return self.all_cards.pop(0)

    # Method for adding cards to a player's hand, either one at a time or multiple if a War is won
    def add_cards(self, new_cards):
        # Add a multiple cards to the hand depending on if the input is a list of multiple won cards
        # otherwise add a singular card from one won card 
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return (f"Player {self.name} has {len(self.all_cards)} cards.")
    
# Method containing the game logic for simulating a full game of war
def war():
    # Instantiate to players
    player_one = Player("One")
    player_two = Player("Two")

    # Instantiate and shuffle a deck
    new_deck = Deck()
    new_deck.shuffle()

    # Deal the deck to both players
    for x in range(26):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())

    game_on = True # game_on variable determines if the game is won and whether to continue playing rounds
    round_num = 0 # round_num variable tracks what round is being played for later analysis

    # While the game has not been won, continue playing through rounds until a player has won
    while game_on:
        round_num += 1
        print(f"Currently on round {round_num}")

        # Determine if either player has run out of cards and the game has been won
        if len(player_one.all_cards) == 0:
            print("Player One is out of cards. Player Two wins!")
            game_on = False
            break
        if len(player_two.all_cards) == 0:
            print("Player Two is out of cards. Player One wins!")
            game_on = False
            break

        # Instantiate the status of cards each player is placing on the table by removing
        # a card from each players hand. Stored as a list in case of War!
        player_one_cards = []
        player_one_cards.append(player_one.remove_one())
        player_two_cards = []
        player_two_cards.append(player_two.remove_one())

        at_war = True # at_war tracks when the actual comparison of played cards is done

        while at_war:
            # If Player One has higher card, they earn the two cards played
            if player_one_cards[-1].value > player_two_cards[-1].value:
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                at_war = False
            # If Player Two has higher card, they earn the two cards played
            elif player_one_cards[-1].value < player_two_cards[-1].value:
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)
                at_war = False
            # If both cards played have the same value, enter War phase
            else:
                print("WAR!")
                # If either player doesn't have enough cards to play War, the other player wins
                # and the game ends
                if len(player_one.all_cards) < 3:
                    print("Player One unable to wage war. Player Two wins!")
                    game_on = False
                    break
                elif len(player_two.all_cards) < 3:
                    print("Player Two unable to wage war. Player One wins!")
                    game_on = False
                    break
                # Play War - each player plays the next three cards in their hands and we repeat
                # the war_on loop (checking last card in list)
                else:
                    for num in range(3):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())

war()