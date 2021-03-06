import unittest
import Spider_Sim

class Test_Card(unittest.TestCase):

    def test_card_accending(self):

        card_1 = Spider_Sim.Card(1, 0)

        card_2 = Spider_Sim.Card(2, 0)

        self.assertRaises(TypeError, card_1.accending(2))

        self.assertTrue(card_1.accending(card_2))

    def test_card_descending(self):

        card_1 = Spider_Sim.Card(1, 0)

        card_2 = Spider_Sim.Card(2, 0)

        self.assertRaises(TypeError, card_1.descending(2))

        self.assertTrue(card_2.descending(card_1))

class Test_Stack(unittest.TestCase):

    def test_stack_pull(self):

        stack = Spider_Sim.Stack([Spider_Sim.Card(10, 0), Spider_Sim.Card(9, 0), Spider_Sim.Card(8, 2), 
                                  Spider_Sim.Card(7, 0), Spider_Sim.Card(6, 0)], False)

        pull_stack = stack.Pull()

        self.assertEqual([Spider_Sim.Card(6, 0), Spider_Sim.Card(7, 0)], pull_stack)

    def test_stack_place(self):

        stack = Spider_Sim.Stack([Spider_Sim.Card(10, 0), Spider_Sim.Card(9, 0), Spider_Sim.Card(8, 2), 
                                  Spider_Sim.Card(7, 0), Spider_Sim.Card(6, 0)])

        moving_cards = [Spider_Sim.Card(4, 0), Spider_Sim.Card(5, 0)]

        stack.Place(moving_cards)

        self.assertEqual([Spider_Sim.Card(10, 0), Spider_Sim.Card(9, 0), Spider_Sim.Card(8, 2), Spider_Sim.Card(7, 0), 
                          Spider_Sim.Card(6, 0), Spider_Sim.Card(5, 0), Spider_Sim.Card(4, 0)],
                          stack.cards)

        wrong_card_suit = [Spider_Sim.Card(3, 1)]
        wrong_card_number = [Spider_Sim.Card(4, 0)]

        raise_stack = Spider_Sim.Stack([Spider_Sim.Card(4, 0)])

        self.assertRaises(Spider_Sim.CannotPlaceError, raise_stack.Place, wrong_card_suit)
        self.assertRaises(Spider_Sim.CannotPlaceError, raise_stack.Place, wrong_card_number)

class Test_Deck(unittest.TestCase):

    def test_deck_constructor(self):

        full_deck = Spider_Sim.Deck(4)
        medium_deck = Spider_Sim.Deck(2)
        low_deck = Spider_Sim.Deck(1)

        for card in low_deck.cards:

            self.assertEqual(card.get_suit(), 0)

        for card in medium_deck.cards:

            try: self.assertEqual(card.get_suit(), 0)

            except(AssertionError): 
                
                self.assertEqual(card.get_suit(), 1)

        for card in full_deck.cards:

            try: self.assertEqual(card.get_suit(), 0)

            except(AssertionError):

                try: self.assertEqual(card.get_suit(), 1)

                except(AssertionError):

                    try: self.assertEqual(card.get_suit(), 2)
                        
                    except(AssertionError):
                        
                        self.assertEqual(card.get_suit(), 3)

    def test_generate_suit(self):

        deck = Spider_Sim.Deck(1)
        suit = deck.Generate_Suit(0)
        i = 0

        for card in suit:

            self.assertEqual(Spider_Sim.Card(i, 0), card)

            i += 1

    def test_deck_deal(self):

        deck = Spider_Sim.Deck(1, 1)

        cards = deck.Deal(1)
        self.assertEqual([Spider_Sim.Card(4, 0)], cards)

        cards = deck.Deal(4)
        self.assertEqual([Spider_Sim.Card(5, 0), Spider_Sim.Card(9, 0), Spider_Sim.Card(9, 0), Spider_Sim.Card(8, 0)], cards)

        deck = Spider_Sim.Deck(1)
        cards = deck.Deal(len(deck.cards))

class Test_Table(unittest.TestCase):

    def test_table_constructor(self):

        table = Spider_Sim.Table(1)

        self.assertEqual(len(table.stacks), 20)

        i = 0
        while i < 10:

            self.assertEqual(table.stacks["O" + str(i)].Length_Check(), 1)

            if i < 4:

                self.assertEqual(table.stacks["H" + str(i)].Length_Check(), 5)

            else:

                self.assertEqual(table.stacks["H" + str(i)].Length_Check(), 4)

            i += 1

    def test_table_spider_deal(self):

        table = Spider_Sim.Table(1)

        table.Spider_Deal()

        i = 0
        while i < 10:

            self.assertEqual(table.stacks["O" + str(i)].Length_Check(), 2)

            if i < 4:

                self.assertEqual(table.stacks["H" + str(i)].Length_Check(), 5)

            else:

                self.assertEqual(table.stacks["H" + str(i)].Length_Check(), 4)

            i += 1

        card = table.stacks["O1"].Pop_Card()
        card = table.stacks["O1"].Pop_Card()

        self.assertRaises(Spider_Sim.StackEmptyError, table.Spider_Deal)


    def test_table_Move(self):

        try:

            table = Spider_Sim.Table(1, 1)

            table.Move("4", "1")

            self.assertEqual(table.stacks["O4"].Length_Check(), 1)
            self.assertEqual(table.stacks["O1"].Length_Check(), 2)
            self.assertEqual(table.stacks["H4"].Length_Check(), 3)
            move_successful = True

        except(Spider_Sim.CannotPlaceError):

            self.assertEqual(table.stacks["O4"].Length_Check(), 1)
            self.assertEqual(table.stacks["O1"].Length_Check(), 1)
            self.assertEqual(table.stacks["H4"].Length_Check(), 4)


if __name__ == "__main__":

    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(Test_Card))
    suite.addTest(unittest.makeSuite(Test_Stack))
    suite.addTest(unittest.makeSuite(Test_Deck))
    suite.addTest(unittest.makeSuite(Test_Table))
    
    unittest.TextTestRunner(verbosity=3).run(suite)


