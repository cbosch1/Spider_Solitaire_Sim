""" Spider Solitaire Simulator
Step 1 - A program that will simulate Spider Solitaire
Step 2 - A program that will run tests on the simulated Spider Solitaire
Step 3 - Profit

Structure:

    Card = (int #, 'Suit')
    Stack = [Cards] + Methods
    Deck = [Cards] + Methods
    Table = Deck, [Stacks], + Methods

"""

class Card(object):
    """Object that allows easy cross comparison
    Number takes int, Suit takes int"""

    def __init__(self, number, suit):

        self.number = number
        self.suit = suit

    def __str__(self):

        string = "Number:" + str(self.get_number()) + ", Suit:" + str(self.get_suit())

        return string

    def __eq__(self, card):

        if type(card) != type(Card(0, 0)):

            return TypeError("Card must be compared with another card object")

        if self.suit == card.get_suit():

            if self.number == card.get_number():

                return True

        return False

    def get_suit(self):

        return self.suit

    def get_number(self):

        return self.number

    def descending(self, card):
        """Compares self to Card object, 
        returns True if card is of same suit, and number of card is one less than self.
        """
        if type(card) != type(Card(0, 0)):

            return TypeError("Card must be compared with another card object")

        if self.suit == card.get_suit():

            if self.number == card.get_number() + 1:

                return True

        return False

    def accending(self, card):
        """Compares self to Card object, 
        returns True if card is of same suit, and number of card is one more than self.
        """
        if type(card) != type(Card(0, 0)):

            return TypeError("Card must be compared with another card object")

        if self.suit == card.get_suit():

            if self.number == card.get_number() - 1:

                return True

        return False
        

class Stack(object):
    """ Contains a list of cards and methods to change that list. """

    def __init__(self, cards, hidden):
        """ Assumes cards are a tuple of int Card Number and string Suit """
        self.cards = cards
        self.hidden = hidden

    def Pull(self):
        """ Returns a reversed list of cards that are of the same suit and in order """

        pull_stack = []

        for i in range(len(self.cards)):

            card_added = False
            current_card = self.cards.pop(len(self.cards) - 1)

            if len(pull_stack) == 0:
                
                pull_stack.append(current_card)

                card_added = True

            next_card = pull_stack[len(pull_stack) - 1]

            if next_card.accending(current_card):

                pull_stack.append(current_card)

                card_added = True

            if card_added == False:

                self.cards.append(current_card)

                return pull_stack
            
        return pull_stack

    def Place(self, cards):
        """Assumes cards is list of Card and either
        Adds cards to own list or
        raise Cannot_Place if cards do not match up 
        Returns none """

        #TODO: Stack.Place
        pass

class Deck(object):
    """ Contains a list of cards and methods to randomly return cards from said list. """

    def __init__(self, num_suit):
        """ Assumes num_suit is int.
        Generates cards as a tuple of int Card Number and string Suit"""
        
        self.cards = []
        self.num_suit = num_suit

        if num_suit == 1:

            for i in range(8):

                self.cards.extend(self.Generate_Suit(0))

        if num_suit == 2:

            for i in range(4):

                for suit in range(2):

                    self.cards.extend(self.Generate_Suit(suit))

        if num_suit == 4:

            for i in range(2):

                for suit in range(4):

                    self.cards.extend(self.Generate_Suit(suit))

        if num_suit != 1 and num_suit != 2 and num_suit != 4:

            raise(ValueError("Incorrect Suit Value"))

    def Generate_Suit(self, suit):
        """ Assists constructor by creating a 13 card list
        with the suit determined by input.
        Returns a list of tuples """

        cards = []

        for card_num in range(13):

            cards.append((card_num, suit))

        return cards


    def Deal(self, num_cards):
        """ Assumes num_cards is int
        Pops a number of cards randomly picked off own list
        Returns those cards as list"""

        #TODO: Deck.Deal

class Table(object):
    """ Contains a list of stacks and a Deck, performs operations to play the game. """

    def __init__(self, num_suit):
        """ Assumes num_suit is int
        Generates Deck and then list of Stacks off num_suit"""

        self.num_suit = num_suit
        self.deck = Deck(num_suit)
        self.stacks = []

    def Spider_Deal(self):
        """ Calls Deck.Deal for each stack on the table
        Raises stack_empty if a stack is empty
        Returns none """

        #TODO: Table.Spider_Deal
        pass
