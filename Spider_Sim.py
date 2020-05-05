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

    def __init__(self, cards):
        """ Assumes cards are a tuple of int Card Number and string Suit """

        #TODO: Stack constructor
        pass

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
        """ Assumes num_suit is int 
        Generates cards as a tuple of int Card Number and string Suit"""
        
        #TODO: Deck constructor
        pass

    def Deal(self, num_cards):
        """ Assumes num_cards is int
        Pops a number of cards randomly picked off own list
        Returns those cards as list"""

        #TODO: Deck.Deal

class Table(object):
    """ Contains a list of stacks and a Deck, performs operations to play the game. """

    def __init__(self, stacks, deck, num_suit):
        """ Assumes num_suit is int
        Generates Deck and then list of Stacks off num_suit"""

        #TODO: Table constructor
        pass

    def Spider_Deal(self):
        """ Calls Deck.Deal for each stack on the table
        Raises stack_empty if a stack is empty
        Returns none """

        #TODO: Table.Spider_Deal
        pass
