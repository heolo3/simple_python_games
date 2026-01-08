import random

# Global variables for storing card suits, ranks, and dictionary for converting ranks to ints for comparison
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

# Card Class for storing individual card representations of suit and rank. Value parameter equates rank parameter (str)
# to int for comparison
class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
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
                created_card = Card(rank, suit)
                self.all_cards.append(created_card)
    
    # Method for shuffling deck utilizing random module
    def shuffle(self):
        random.shuffle(self.all_cards)
  
    # Method for dealing single card to player(s)
    def deal_one(self):
        return self.all_cards.pop()

class Player:

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hand = []
        self.bet = 0

    def wager(self, amount):
        if(self.money - amount < 0):
            print("You don't have enough money left to bet that amount!")
        else:
            self.money -= amount
            self.bet = amount
            print(f"{self.name} bet ${self.bet}")

    def print_hand(self):
        print("Player's hand: ")
        for card in self.hand:
            print(f"\t{card} : {card.value}")
    
    def sum_hand(self):
        sum = 0
        for card in self.hand:
            sum += card.value
        return sum
    
    def player_choice(self):
        try:
            player_choice = str(input("Would you like to Hit or Stand? "))
        except TypeError:
            print("Expecting input of either \"Hit\" or \"Stand\"")
        
        return player_choice
    

class Dealer:

    def __init__(self):
        self.hand = []

    def print_hand_preflip(self):
        print("Dealer's hand: ")
        print(f"\t{self.hand[0]} : {self.hand[0].value}")

    def print_hand_postflip(self):
        print("Dealer's hand: ")
        for card in self.hand:
            print(f"\t{card} : {card.value}")

    def sum_hand(self):
        sum = 0
        for card in self.hand:
            sum += card.value
        return sum



def blackjack():
    still_playing = True
        
    while still_playing == True:
        # Create a player with name and initial money value
        player = Player("Graeme", 50)

        # Create a Dealer
        dealer = Dealer()

        # Create a deck of 52 cards
        deck = Deck()

        # Shuffle the deck
        deck.shuffle()

        # Ask the Player for their bet
        # Make sure that the Player's bet does not exceed their available chips
        bet_amount = 0
        try:
            bet_amount = int(input("Place your wager: $"))
            player.wager(bet_amount)
        except TypeError:
            pass

        # Deal two cards to the Dealer and two cards to the Player
        for n in range(2):
            player.hand.append(deck.deal_one())
            dealer.hand.append(deck.deal_one())

        # Show only one of the Dealer's cards, the other remains hidden
        dealer.print_hand_preflip()

        # Show both of the Player's cards
        player.print_hand()

        # Ask the Player if they wish to Hit, and take another card
        # If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
        player_hand_sum = player.sum_hand()
        player_choice = player.player_choice()

        while player_hand_sum <= 21 and player_choice == "Hit":    
            player.hand.append(deck.deal_one())
            player.print_hand()
            player_hand_sum = player.sum_hand()
            player_choice = player.player_choice()

        # If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
        if player_choice == "Stand":
            dealer.print_hand_postflip()

            dealer_hand_sum = dealer.sum_hand()
            while dealer_hand_sum < 17:
                dealer.hand.append(deck.deal_one())
                dealer_hand_sum = dealer.sum_hand()


        # Determine the winner and adjust the Player's chips accordingly
        print("------------------------")
        player.print_hand()
        dealer.print_hand_postflip()

        if player_hand_sum > 21:
            print(f"PLAYER BUST! The House has won. {player.name} lost ${player.bet}")
        elif dealer_hand_sum > 21:
            print(f"HOUSE BUST! Congrats, {player.name} won ${player.bet}")
            player.money += player.bet*2
        elif player_hand_sum > dealer_hand_sum:
            print(f"Congrats, {player.name} won ${player.bet}")
            player.money += player.bet*2
        else:
            print(f"The House has won. {player.name} lost ${player.bet}")
            
        print(f"{player.name} has ${player.money}")

    # Ask the Player if they'd like to play again
        try:
            yes_no = str(input("Would you like to play again? Y/n "))
            if yes_no == "Y":
                still_playing = True
            elif yes_no == "n":
                still_playing = False
            else:
                print("Expecting Y/n")
        except TypeError:
            print("Expecting Y/n")
    

blackjack()