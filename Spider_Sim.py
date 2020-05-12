import random
""" Spider Solitaire Simulator
Step 1 - A program that will simulate Spider Solitaire
Step 2 - A program that will run tests on the simulated Spider Solitaire
Step 3 - Profit

Structure:

    Card = int card_# + int card_suit + Methods
    Stack = [Cards] + Methods
    Deck = [Cards] + Methods
    Table = Deck, [Stacks], + Methods

"""

class CannotPlaceError(Exception):

    """Exception raised for when a stack move cannot place any cards.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message

class StackEmptyError(Exception):

    """Exception raised for when a deal cannot place a card on an empty stack.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message

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
        if not isinstance(card, Card):

            return TypeError("Card must be compared with another card object")

        if self.suit == card.get_suit():

            if self.number == card.get_number() + 1:

                return True

        return False

    def accending(self, card):
        """Compares self to Card object, 
        returns True if card is of same suit, and number of card is one more than self.
        """
        if not isinstance(card, Card):

            return TypeError("Card must be compared with another card object")

        if self.suit == card.get_suit():

            if self.number == card.get_number() - 1:

                return True

        return False
        

class Stack(object):
    """ Contains a list of cards and methods to change that list. """

    def __init__(self, cards, hidden=False):
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

        for i in range(len(cards)):

            card_added = False

            current_card = cards.pop(len(cards) - 1)

            bottom_stack = self.cards[len(self.cards) - 1]

            if bottom_stack.descending(current_card):

                self.cards.append(current_card)

                card_added = True

            elif not card_added:

                raise CannotPlaceError("Cannot place cards on stack")

    def Add_Card(self, card):

        if isinstance(card, Card):

            self.cards.append(card)

    def Pop_Card(self):
        """Returns last card as it is poped off list"""

        return self.cards.pop()

    def Length_Check(self):

        return len(self.cards)

    def Copy(self):
        """ Copy's self with newly generated list to prevent accidental editing.
        Returns Stack object"""

        copy_cards = []

        for card in self.cards:

            copy_cards.append(card)

        return Stack(copy_cards, self.hidden)

class Deck(object):
    """ Contains a list of cards and methods to randomly return cards from said list. """

    def __init__(self, num_suit, seed=0):
        """ Assumes num_suit is int.
        Generates cards as a tuple of int Card Number and string Suit"""
        
        self.num_suit = num_suit
        self.seed = seed
        self.cards = []

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

            cards.append(Card(card_num, suit))

        return cards


    def Deal(self, num_cards):
        """ Assumes num_cards is int
        Pops a number of cards randomly picked off own list
        Returns those cards as list"""

        if self.seed != 0:
            
            random.seed(self.seed)

        else:

            random.seed(None)

        cards = []

        for i in range(num_cards):

            end = len(self.cards) - 1

            if end != 0:
                
                cards.append(self.cards.pop(random.randint(0, end)))

        return cards

class Table(object):
    """ Contains a list of stacks and a Deck, performs operations to play the game. """

    def __init__(self, num_suit, seed=0):
        """ Assumes num_suit is int
        Generates Deck and then list of Stacks off num_suit"""

        self.num_suit = num_suit
        self.deck = Deck(num_suit, seed)
        self.stacks = {}

        i = 0
        while i < 4:

            self.stacks["H"+str(i)] = Stack(self.deck.Deal(5), True)
            self.stacks["O"+str(i)] = Stack(self.deck.Deal(1))
            i += 1

        while i < 10:

            self.stacks["H"+str(i)] = Stack(self.deck.Deal(4), True)
            self.stacks["O"+str(i)] = Stack(self.deck.Deal(1))
            i += 1

    def Spider_Deal(self):
        """ Calls Deck.Deal for each stack on the table
        Raises stack_empty if a stack is empty
        Returns none """

        for stack in self.stacks.values():

            if not stack.hidden:

                if stack.Length_Check() > 0:
                    
                    stack.Add_Card(self.deck.Deal(1).pop())

                else:

                    raise StackEmptyError("Cannot deal card to empty stack")

    def Move(self, stack_1_number, stack_2_number):
        """ Attempts to move cards from stack_1 to stack_2.
        Takes in two strings, expects they are the number of the stack.
        """

        stack_1 = self.stacks["O" + stack_1_number].Copy()
        stack_2 = self.stacks["O" + stack_2_number].Copy()

        cards = stack_1.Pull()
            
        stack_2.Place(cards)

        self.stacks["O" + stack_1_number] = stack_1.Copy()
        self.stacks["O" + stack_2_number] = stack_2.Copy()

        if stack_1.Length_Check() == 0:

            card = self.stacks["H" + stack_1_number].Pop_Card()

            self.stacks["O" + stack_1_number].Add_Card(card)