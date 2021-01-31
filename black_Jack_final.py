from IPython.display import clear_output as co
import random

#CLASSES

# Class for card


#Randomizes the order of the deck list
    # def shuffle(self):  
    #     random.shuffle(self.deck)

    # # deal function   
    # # def deal(self):

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
            
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
        
    
 #Class for Dealer
class Dealer:
    dealer_cards = []
    def __init__(self, dealer_cards):
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
    def __init__(self, player_cards):
        while len(player_cards) != 2:
            player_cards.append(random, randit(1, 13))
            if len(player_cards) == 2:
                print("You have: ", player_cards)
                continue
            if sum(player_cards) == 21:
                print("You win")
            elif sum(player_cards) > 21:
                print("You bust")
        
        while sum(player_cards) < 2:
            next_move = str(input)("Select 'stay' or 'hit' ").lower()
            if next_move == "hit":
                player_cards.append(random, randit(1, 13))
                #show cards
                print("Your new hand total is " + str(sum(player_cards)) + ", your cards are ," + player_cards)
            else:
                print("The dealer has: " + str(sum(dealer_cards)))
                print("You have: " + str(sum(player_cards)) + ", your cards are " + str(player_cards))


suits = ('Clubs', 'Diamonds', 'Spades', 'Hearts ')
ranks = ('one', 'two', 'three', 'four', 'five', 'six', 'seven',
         'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen')
value = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,'nine': 9, 'ten': 10, 'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}
    
#FUNCTIONS
   
#hit or stand
def hit_stand():
    pass


# Player
# Dealer


# Green colors = Class definitions / Comments
# Blue colors = Booleans / python internal functions
# Yellow colors = Function names (example: print, play, main, etc.)
# Orange colors = Strings
# White colors = Variables or objects 
# Purple colors = pass / continue / if / else / for / while Conditionals

class Game:
    # Self is passed into class definitions
    def __init__(self):
        return

    def play(self):
        self.playing = True

class Card:
    # Individual cards of suit and rank
    # intializing the card to its suit and rank
    def __init__(self, suit, rank): 
        self.suit = suit
        self.rank = rank
    # When you print this class out it prints out this definition
    def turn_to_string(self):
        return str(self.rank) + ' of ' + self.suit

class Deck:
    # Deck of 52 Card(s)
    def __init__(self):
        # Place to keep all the cards
        self.deck = [] 
        suits = [
            'Clubs', 'Diamonds', 'Spades', 'Hearts '
        ]
        ranks = [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
        ]

        # Go through all the suits and ranks and push into deck
        for x in suits:
            for y in ranks:
                card_object = Card(x, y)
                self.deck.append(card_object)

    def shuffle(self):
        # randomizes the cards in self.deck
        random.shuffle(self.deck)



class Dealer:
    def __init__(self):
        # Set dealer cards to passed in deck
        self.dealer_hand = []

    def deal_hand(self, deck):
        # Pamaters: deck is a object of Deck class

        # Take 2 cards from deck. Give to self
        card_object_1 = deck.pop()
        card_object_2 = deck.pop()
        self.dealer_hand = [card_object_1, card_object_2]

        # Take 2 cards from deck. Give to player
        card_object_1_player = deck.pop()
        card_object_2_player = deck.pop()
        player_hand = [card_object_1_player, card_object_2_player]
        # Returning the list of of 2 cards given to the player
        return player_hand

    def deal_hit(self, deck):
        # Give a card to player
        hit_card = deck.pop()
        # Returning the card popped from the deck for a hit
        return hit_card

    def count_cards(self):
        # player hand has x amount of cards in it. 
        # list of card objects -> getting the first card -> getting first card rank
        sum_of_cards = 0
        for card in self.dealer_hand:
            sum_of_cards = sum_of_cards + card.rank
        return sum_of_cards


class Player:
    def __init__(self, two_card_hand):
        # two_card_hand: list of 2 card objects
        # example: player_hand = [seven of diamonds, one of clubs]
        self.player_hand = two_card_hand

    def count_cards(self):
        # player hand has x amount of cards in it. 
        # list of card objects -> getting the first card -> getting first card rank
        sum_of_cards = 0
        for card in self.player_hand:
            sum_of_cards = sum_of_cards + card.rank
        return sum_of_cards

    def take_hit(self, card):
        # player takes card from dealer and keeps it in hand
        self.player_hand.append(card)
        return

def main():
    # Creating an object out of a class
    # Creating something from a class creates an object
    game_object = Game()

    # Utilizing object functions defined in the class
    game_object.play()

    # # Working with card class
    # suit = "hearts"
    # rank = "jack"
    # card_object_1 = Card(suit, rank)
    # card_object_2 = Card("king", "diamonds")

    # Create the deck
    deck_object = Deck()
    deck_object.shuffle()

    # Create the dealer
    dealer_object = Dealer()
    # Dealer deals hand to player
    player_hand_cards = dealer_object.deal_hand(deck_object.deck)

    # Create the player
    player_object = Player(player_hand_cards)

    # Ask for hit from dealer
    hit_card = dealer_object.deal_hit(deck_object.deck)
    # Player puts card in hand
    player_object.take_hit(hit_card)

    print(player_object.count_cards())

    print("-------- Players hands --------")
    for card in player_object.player_hand:
        print(card.turn_to_string())
    
    print("-------- Delears hands --------")
    for card in dealer_object.dealer_hand:
        print(card.turn_to_string())


    print("------ Deck amount left: -------")
    print(len(deck_object.deck))

    if(player_object.count_cards() > 21):
        print("------------DEALER WINS-----------")

    else:
        if(player_object.count_cards() > dealer_object.count_cards()):
            print("------------PLAYER WINS-----------")
        else:
            print("------------DEALER WINS-----------")



if _name_ == "_main_":
    main()