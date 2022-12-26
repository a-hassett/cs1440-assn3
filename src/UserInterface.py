from math import floor  	         	  

from Deck import Deck
from Menu import Menu  	         	  
from MenuOption import MenuOption  	         	  


class UserInterface():  	         	  
    """  	         	  
    Sets up all of the data that the user will interact with 	         	  
    """

    def __init__(self):  	         	  
        self.__m_currentDeck = None  	         	  
        self.__m_menu = Menu("Main")  	         	  
        self.__m_menu += MenuOption("C", "Create a new deck")  	         	  
        self.__m_menu += MenuOption("X", "Exit the program")  	         	  

    # start the program by asking whether to make a deck or exit
    # proceed accordingly
    def run(self):  	         	  
        print("Welcome to the Bingo Deck Generator\n")

        while True:  	         	  
            command = self.__m_menu.prompt()  	         	  
            if command.upper() == "C":  	         	  
                self.__create_deck()  	         	  
            elif command.upper() == "X":  	         	  
                break  	         	  

    # represent the deck menu and prompt the user for further action
    def __deck_menu(self):
        menu = Menu("Deck")
        menu += MenuOption("P", "Print a card to the screen")  	         	  
        menu += MenuOption("D", "Display the whole deck to the screen")  	         	  
        menu += MenuOption("S", "Save the whole deck to a file")  	         	  
        menu += MenuOption("X", "Return to the Main menu")  	         	  

        while True:  	         	  
            command = menu.prompt()  	         	  
            if command.upper() == "P":  	         	  
                self.__print_card()  	         	  
            elif command.upper() == "D":  	         	  
                print(self.__m_currentDeck)  	         	  
            elif command.upper() == "S":  	         	  
                self.__save_deck()  	         	  
            elif command.upper() == "X":  	         	  
                break  	         	  

    # return a string from the user
    # validate that it is not empty
    def __get_str(self, prompt):  	         	  
        while True:
            strValue = input(prompt)
            if strValue != "":
                return strValue

    # return an integer from the user
    # validate it is in the range from lo to hi; if not, ask for a new input
    def __get_int(self, prompt, lo, hi):  	         	  
        while True:
            intValue = input(prompt)
            if intValue.isnumeric() and lo <= int(intValue) <= hi:
                return int(intValue)

    # create a deck to store in self.__m_currentDeck
    # prompt user for size of Bingo card, number of cards in deck, and the deck's maximum number
    def __create_deck(self):  	         	  
        cardSize = self.__get_int("Enter your Bingo card size (3 to 16): ", 3, 16)
        numCards = self.__get_int("Enter number of cards in your deck (2 to 8192): ", 2, 8192)
        maxNum = self.__get_int(f"Enter the maximum number allowed (0 to {floor(3.9 * cardSize * cardSize)}): ", 0, floor(3.9 * cardSize * cardSize))
        self.__m_currentDeck = Deck(cardSize, numCards, maxNum)

        # once we make the deck, we ask the user what to do with it
        self.__deck_menu()

    # print a single card from the deck and prompt user for which one
    def __print_card(self):  	         	  
        cardId = self.__get_int(f"Number of desired card (0 to {len(self.__m_currentDeck) - 1}): ", 0, len(self.__m_currentDeck) - 1)
        print(self.__m_currentDeck.card(cardId))

    # save the deck to a file
    # prompt the user for a valid file; this shouldn't crash when given files!
    def __save_deck(self):
        while True:
            filename = self.__get_str("Name of file to write the Deck into: ")
            try:
                file_tst = open(filename)
                file_tst.close()
                break
            # checking for invalid files
            except FileNotFoundError:
                pass

        file = open(filename, "w")
        file.write(self.__m_currentDeck.__str__())
        file.close()
