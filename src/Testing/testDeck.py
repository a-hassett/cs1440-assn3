# Tests the Deck Class  	         	  

import unittest  	         	  
import Deck  	         	  


class TestDeck(unittest.TestCase):  	         	  
    def setUp(self):  	         	  
        size = 7  	         	  
        self.deck2 = Deck.Deck(card_size=size, num_cards=2, max_num=3*size*size)  	         	  

        size = 16  	         	  
        self.deck16 = Deck.Deck(card_size=size, num_cards=16, max_num=3*size*size)  	         	  

        self.deck8192 = Deck.Deck(card_size=size, num_cards=8192, max_num=3*size*size)  	         	  

    def test_len(self):  	         	  
        """Ensure that Decks contain expected number of cards"""  	         	  
        self.assertEqual(len(self.deck2), 2)  	         	  
        self.assertEqual(len(self.deck16), 16)  	         	  
        self.assertEqual(len(self.deck8192), 8192)  	         	  

    def test_card(self):  	         	  
        """Ensure that Cards can be accessed from within a Deck"""  	         	  

        # In my implementation, an attempt to get a non-existent card results in `None`  	         	  
        # Cards are indexed by their ID number  	         	  

        self.assertIsNotNone(self.deck2.card(0))
        self.assertIsNotNone(self.deck2.card(1))  	         	  
        self.assertIsNone(self.deck2.card(2))

        self.assertIsNotNone(self.deck16.card(0))
        self.assertIsNotNone(self.deck16.card(8))  	         	  
        self.assertIsNone(self.deck16.card(16))

        self.assertIsNone(self.deck8192.card(-1))
        self.assertIsNotNone(self.deck8192.card(4096))  	         	  
        self.assertIsNotNone(self.deck8192.card(8191))
        self.assertIsNone(self.deck8192.card(8192))


if __name__ == '__main__':  	         	  
    unittest.main()  	         	  
