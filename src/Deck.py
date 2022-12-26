from Card import Card  	         	  
from RandNumberSet import RandNumberSet  	         	  


class Deck():  	         	  
    def __init__(self, card_size, num_cards, max_num):
        """
        Set up the deck and fill it with instances of Cards
        """
        self.__card_size = card_size
        self.__num_cards = num_cards
        self.__cards = []

        # give random bunch of numbers to the deck
        for id in range(num_cards):
            randomSet = RandNumberSet(card_size, max_num)
            randomSet.shuffle()
            self.__cards.append(Card(id, randomSet))

    def __len__(self):
        return self.__num_cards

    # return string of nicely formatted card
    def card(self, n):
        if not 0 <= n < self.__num_cards:
            return None
        else:
            return self.__cards[n]

    # return string of nicely formatted cards all squished together
    def __str__(self):
        entireDeck = ""
        for obj in self.__cards:
            entireDeck += obj.__str__() + "\n"

        return entireDeck

