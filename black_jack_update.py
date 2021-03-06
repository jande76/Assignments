from IPython.display import clear_output as co
import random

suits = ('Clubs', 'Diamonds', 'Spades', 'Hearts ')
ranks = ('one', 'two', 'three', 'four', 'five', 'six', 'seven',
         'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen')
value = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,'nine': 9, 'ten': 10, 'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}
     
playing = True

# Class for card
class Card:
    def __init__(self, suit, rank):    
       self.suit = suit
       self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

# Class for the deck
class Deck:
    def __init__(self,):
        self.deck = [] 
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

#Turns deck obj into strings
    def __str__(self):
        deck_cons = '' 
        for card in self.decks:
            deck_cons += '\n' card.__str__()
        return deck_cons 

#Randomizes the order of the deck list
    def shuffle(self)  
        random.shuffle(self.deck)

#picking a card from deck
    def deal(self)
        one_card = self.deck.pop()
        return one_card

class Hand: 
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def add_card(self, card):
        self.cards.append(card)
        self.values += values[card.rank]
        if card.rank == 'ace':
            self.aces += 1
            
    def adjust_for_ace(self)
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
        
    
 #Class for Dealer


class Dealer:
dealer_cards = []
    def __init__(self, dealer_cards)
# function to deal the cards and only show one card at a time
    while len(dealer_cards) != 2:
        # picks random integer card between 1 and 13 and adds it to the empty list
        dealer_cards.append(random, randit(1, 13))
        if len(dealer_cards) == 2:
            print("The dealer has _ and: ", dealer_cards[1])
            continue
        if sum(dealer_cards) == 21:
            print("Dealer wins")
        elif sum(dealer_cards) > 21:
            print("Dealer busts")

# Class for the player(dealer)

class Player:
player_cards = []
   def __init__(self, player_cards)
       while len(player_cards) != 2:
            player_cards.append(random, randit(1, 13))
        if len(player_cards) == 2:
            print("You have: ", player_cards)
        continue
        if sum(player_cards) == 21:
            print("You win")
        elif sum(player_cards) > 21:
            print("You bust")
        
        while sum(player_cards) < 2
            next_move = str(input)("Select 'stay' or 'hit' ").lower()
                if next_move == "hit":
                    player_cards.append(random, randit(1, 13))
                    #show cards
                    print("Your new hand total is " str(sum(player_cards)) + ", your cards are ", player_cards))
                else:
                    print("The dealer has: ", str(sum(dealer_cards))
                    print("You have: ", str(sum(player_cards)) + ", ", your cards are ", player_cards))
   
#hit or stand
class Hit_Or_Stand:
    
    def hit(deck, hand):
        hand.add_card(deck.deal())
        hand.adjust_for_ace()

    def hit_and_stand(deck, hand):

        while True:
            ask = input("Are you going to hit or stand? Enter 'hit' or 'stand.' ")

            if ask[0].lower() == 'hit':
                hit(deck, hand)
            elif ask[0].lower() == 'stand':
                print("You are choosing to stand. It's the dealer's turn.")
                playing = False
            else:
                print("Plase seelect a valid command, 'hit or 'stand'")
                continue
            break

    while not game_Over:
