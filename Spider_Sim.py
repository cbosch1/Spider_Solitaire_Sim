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

class Stack(object):
    """ Contains a list of cards and methods to change that list. """

    def __init__(self, cards, hidden):
        """ Assumes cards are a tuple of int Card Number and string Suit """
        self.cards = cards
        self.hidden = hidden

    def Pull(self):
        """ Returns list of cards that are of the same suit and in order """

        #TODO: Stack.Pull
        pass

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
