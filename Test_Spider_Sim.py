import unittest
import Spider_Sim

class Test_Stack(unittest.TestCase):

    def test_stack_constructor(self):

        self.assertEqual(1, 2)

    def test_stack_pull(self):

        self.assertEqual(1, 2)

    def test_stack_place(self):

        self.assertEqual(1, 2)

class Test_Deck(unittest.TestCase):

    def test_deck_constructor(self):

        full_deck = Spider_Sim.Deck(4)
        medium_deck = Spider_Sim.Deck(2)
        low_deck = Spider_Sim.Deck(1)

        for card in low_deck.cards:

            self.assertEqual(card[1], 0)

        for card in medium_deck.cards:

            try: self.assertEqual(card[1], 0)

            except(AssertionError): 
                
                self.assertEqual(card[1], 1)

        for card in full_deck.cards:

            try: self.assertEqual(card[1], 0)

            except(AssertionError):

                try: self.assertEqual(card[1], 1)

                except(AssertionError):

                    try: self.assertEqual(card[1], 2)
                        
                    except(AssertionError):
                        
                        self.assertEqual(card[1], 3)

    def test_generate_suit(self):

        deck = Spider_Sim.Deck(1)
        suit = deck.Generate_Suit(0)
        i = 0

        for card in suit:

            self.assertTupleEqual((i, 0), card)

            i += 1

    def test_deck_deal(self):

        self.assertEqual(1, 2)

class Test_Table(unittest.TestCase):

    def test_table_constructor(self):

        self.assertEqual(1, 2)

    def test_table_spider_deal(self):

        self.assertEqual(1, 2)

if __name__ == "__main__":

    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(Test_Stack))
    suite.addTest(unittest.makeSuite(Test_Deck))
    suite.addTest(unittest.makeSuite(Test_Table))
    
    unittest.TextTestRunner(verbosity=3).run(suite)


