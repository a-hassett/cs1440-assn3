import unittest  	         	  

from Card import Card  	         	  
from RandNumberSet import RandNumberSet  	         	  


class TestCard(unittest.TestCase):  	         	  

    def setUp(self):  	         	  
        idnum, size = 0, 3  	         	  

        self.card0 = Card(idnum, RandNumberSet(size, size*size*4))  	         	  

        idnum, size = 1, 5  	         	  
        self.card1 = Card(idnum, RandNumberSet(size, size*size*4))  	         	  

        idnum, size = 2, 16  	         	  
        self.card2 = Card(idnum, RandNumberSet(size, size*size*4))  	         	  

        idnum, size = 3, 8  	         	  
        self.card3 = Card(idnum, RandNumberSet(size, size*size*4))  	         	  


    def test_len(self):  	         	  
        """Assert that card size is as expected"""  	         	  
        self.assertEqual(len(self.card0), 3)  	         	  
        self.assertEqual(len(self.card1), 5)  	         	  
        self.assertEqual(len(self.card2), 16)  	         	  
        self.assertEqual(len(self.card3), 8)  	         	  

    def test_id(self):  	         	  
        """Assert that card ID number is as expected"""  	         	  
        self.assertIsNotNone(self.card0)  	         	  
        self.assertEqual(self.card0.id(), 0)  	         	  

        self.assertIsNotNone(self.card1)  	         	  
        self.assertEqual(self.card1.id(), 1)  	         	  

        self.assertIsNotNone(self.card2)  	         	  
        self.assertEqual(self.card2.id(), 2)  	         	  

        self.assertIsNotNone(self.card3)  	         	  
        self.assertEqual(self.card3.id(), 3)  	         	  

    def test_freeSquares(self):  	         	  
        """Ensure that odd-numbered cards have 1 "Free!" square in the center"""  	         	  
        # Check every single square of the 3x3 card  	         	  
        self.assertIsInstance(self.card0.number_at(0, 0), int)  	         	  
        self.assertIsInstance(self.card0.number_at(0, 1), int)  	         	  
        self.assertIsInstance(self.card0.number_at(0, 2), int)  	         	  
        self.assertIsInstance(self.card0.number_at(1, 0), int)  	         	  
        self.assertIsInstance(self.card0.number_at(1, 1), str)  	         	  
        self.assertIsInstance(self.card0.number_at(1, 2), int)  	         	  
        self.assertIsInstance(self.card0.number_at(2, 0), int)  	         	  
        self.assertIsInstance(self.card0.number_at(2, 1), int)  	         	  
        self.assertIsInstance(self.card0.number_at(2, 2), int)  	         	  

        # Examine the 3x3 region at the center of this card  	         	  
        self.assertIsInstance(self.card1.number_at(1, 1), int)  	         	  
        self.assertIsInstance(self.card1.number_at(1, 2), int)  	         	  
        self.assertIsInstance(self.card1.number_at(1, 3), int)  	         	  
        self.assertIsInstance(self.card1.number_at(2, 1), int)  	         	  
        self.assertIsInstance(self.card1.number_at(2, 2), str)  	         	  
        self.assertIsInstance(self.card1.number_at(2, 3), int)  	         	  
        self.assertIsInstance(self.card1.number_at(3, 1), int)  	         	  
        self.assertIsInstance(self.card1.number_at(3, 2), int)  	         	  
        self.assertIsInstance(self.card1.number_at(3, 3), int)  	         	  

        # Examine the 2x2 region around the "center" of the even-numbered cards  	         	  
        self.assertIsInstance(self.card2.number_at(7, 7), int)  	         	  
        self.assertIsInstance(self.card2.number_at(7, 8), int)  	         	  
        self.assertIsInstance(self.card2.number_at(8, 7), int)  	         	  
        self.assertIsInstance(self.card2.number_at(8, 8), int)  	         	  

        self.assertIsInstance(self.card3.number_at(3, 3), int)  	         	  
        self.assertIsInstance(self.card3.number_at(3, 4), int)  	         	  
        self.assertIsInstance(self.card3.number_at(4, 3), int)  	         	  
        self.assertIsInstance(self.card3.number_at(4, 4), int)  	         	  

    def test_no_duplicates(self):  	         	  
        """Ensure that cards do not contain duplicate numbers"""  	         	  

        # Because numbers are randomly assigned there *may* be a chance that a  	         	  
        # duplicate slips through.  Without auditing the source code, we can't  	         	  
        # prove there is no possibility this could happen.  The best we can do  	         	  
        # with an automated test is to generate a bunch of cards, check them all  	         	  
        # for duplicates until we are confident enough  	         	  

        print()  	         	  
        size = 16  	         	  
        for i in range(10001):  	         	  
            # The largest card with the smallest allowed RandNumberSet gives the  	         	  
            # highest probability of a repeated number, if that is possible  	         	  

            if i % 1000 == 0:  	         	  
                print(f"Searching for a card with a duplicate number #{i}...")  	         	  

            seen = set()  	         	  

            c = Card(i, RandNumberSet(size, size*size*2))  	         	  
            for row in range(size):  	         	  
                for col in range(size):  	         	  
                    n = c.number_at(row, col)  	         	  
                    self.assertNotIn(n, seen)  	         	  
                    seen.add(n)  	         	  


if __name__ == '__main__':  	         	  
    unittest.main()  	         	  
