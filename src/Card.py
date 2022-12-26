class Card():  	         	  
    COLUMN_NAMES = list("BINGODARLYZEMPUX")  	         	  

    def __init__(self, idnum, ns):  	         	  
        """  	         	  
        Initialize a Bingo! card  	         	  
        """

        self.__idnum = idnum
        self.__numberSet = ns

    def id(self):  	         	  
        return self.__idnum

    # return what will be in Bingo boxes, whether it's a number or "FREE!"
    def number_at(self, row, col):  	         	  
        if len(self) % 2 == 1 and col == len(self) // 2 and row == len(self) // 2:
            return "FREE!"
        else:
            return self.__numberSet[row][col]  # uses RandNumberSet's list product

    # return size of Bingo card, N, when used with the length operator len()
    def __len__(self):  	         	  
        return len(self.__numberSet)

    # return a nicely formatted string of a Bingo card
    def __str__(self):  	         	  
        finalBoard = ""
        finalBoard += f"Card #{self.__idnum}"
        finalBoard += "\n"
        for n in range(len(self)):
            finalBoard += format(Card.COLUMN_NAMES[n], ">4s") + "  "
        finalBoard += " \n"
        finalBoard += self.printBoardLine(len(self)) + "\n"
        for row in range(len(self)):
            for col in range(len(self)):
                finalBoard += "|"
                finalBoard += format(str(self.number_at(row, col)), "^5s")
            finalBoard += "|\n"
            finalBoard += self.printBoardLine(len(self)) + "\n"

        return finalBoard

    # return a string of the size horizontal board borders
    def printBoardLine(self, width):
        line = ""
        for i in range(width):
            line += "+-----"
        line += "+"

        return line
