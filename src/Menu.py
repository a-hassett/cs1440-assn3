class Menu():  	         	  
    def __init__(self, szHeader):
        """  	         	  
        Create a menu with options to choose from         	  
        """

        self.__m_szHeader = szHeader  	         	  
        self.__m_options = []  	         	  

    # append options to the menu externally
    def __iadd__(self, option):  	         	  
        self.__m_options.append(option)
        return self  	         	  

    # choose a certain option using an indexing operator []
    def __getitem__(self, nIdx):  	         	  
        if 0 <= nIdx < len(self):
            return self.__m_options[nIdx]  	         	  
        else:  	         	  
            raise IndexError  	         	  

    def __len__(self):  	         	  
        return len(self.__m_options)

    # check if user input is a command in the menu
    def bIsValidCommand(self, chCommand):  	         	  
        for i in range(len(self)):
            if chCommand.upper() == self[i].chCommand().upper():  	         	  
                return True  	         	  
        return False  	         	  

    # ask user their choice of command
    def prompt(self):  	         	  
        while True:
            options = []  	         	  

            # print menu for user
            print(f"\n{self.__m_szHeader} menu:")  	         	  
            for i in range(len(self)):  	         	  
                option = self[i]  # pulls from menu
                if option is not None:  	         	  
                    print(f"{option.chCommand()} - {option.szDescription()}")  	         	  
                    options += option.chCommand()  	         	  

            # ask user for choice
            print(f"\nEnter a {self.__m_szHeader} command ({', '.join(options)})")  	         	  
            command = input()  	         	  
            if self.bIsValidCommand(command):  	         	  
                return command  	         	  
            else:  	         	  
                print(f"'{command.strip()}' is not a valid option")  	         	  
