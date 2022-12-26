class MenuOption():  	         	  
    def __init__(self, chCommand, szDescription):
        """  	         	  
        Create a MenuOption that is a letter with a description  	  
        """

        # if option letter or description is empty, print question marks instead
        self.__m_chCommand = chCommand  	         	  
        if self.__m_chCommand == '':  	         	  
            self.__m_chCommand = '?'  	         	  
        elif len(self.__m_chCommand) > 1:  	         	  
            self.__m_chCommand = self.__m_chCommand[0]  	         	  

        self.__m_szDescription = szDescription  	         	  
        if self.__m_szDescription == '':  	         	  
            self.__m_szDescription = '???'  	         	  

    # return a string of the option letter
    def chCommand(self):  	         	  
        return self.__m_chCommand

    # return a string of the option description
    def szDescription(self):  	         	  
        return self.__m_szDescription

    # return a string of the option letter and description combined
    def __str__(self):  	         	  
        return f"{self.__m_chCommand} {self.__m_szDescription}"
