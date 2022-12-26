# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**

* A detailed written description of the problem this program aims to solve.
* Describe what a *good* solution looks like.
    * List what you already know how to do.
    * Point out any challenges that you can foresee.

This program will print varying-sized Bingo cards. It will have a deck of a certain
number of cards. Once you have this deck, you can print one single card,
print every card in the deck, or save the deck as a text file. To produce
the cards, we must prompt the user for the size of the card N (from 3x3 to 16x16).
Then we use this size and provide a range of numbers to be the highest possible
number on the Bingo card. This range M (from 2 x N^2 to floor(3.9 x N^2)) is 
provided to the user where they can choose. So, we need two user inputs. We
will need to label the bingo card so that each column is labeled a new letter
in the word "BINGODARLYZEMPUX". Thankfully, this is already provided in the 
Card.py starter code. In each of these columns, there will be randomly selected
number from 1/N of the range of largest numbers. In other words, column B will
contain numbers from the smallest 1/16th of the possible values of M in a 16x16
Bingo card. The next column would contain the next 1/16th. I think I could do
this by getting user input for N between 3 and 16. I will reject bad input.
Then I prompt them for an integer M between 2 x N^2 and floor(3.9 x N^2). I will
again reject bad input. I will then make a list of every integer between 1
and M to represent every possible number that could be on that deck of Bingo
cards. Then I will break this list up into columns of the Bingo card by flooring
1/N. I can make a for loop with i that repeats N times where indexes 0 to floor(1/N) get
removed from the original list and are appended to the i index of a new list.
Each index here will represent a column of the Bingo card. When making the cards,
I will choose numbers to be in each column based on the second list I made.
I will have to check that each number isn't already printed. I thought about
removing a number from the list as I used it, but I think this would be inefficient
because I have to make multiple cards for the deck. I'll also have to check
if N is odd, because if it is, the middle square of the Bingo card with be FREE.
We ask for user input once again to determine how many cards will be in the deck.
It will be an integer between 2 and 8192. I have to be able to keep track of
each card's numbers and their position in the deck. The easiest way to track their
numbers is to use multiple instances of a Card class, but I don't know how to make
multiple different names for different classes without presetting them. Maybe
I'll be able to make a string that will change as I move through a for loop. 
I think I could also make the Card class a subclass of a Deck class so that I'll
be able to ask for the properties of the deck when working with a card. I'll
also have to keep track of the position of each card, probably with a list again.
This means I'll have to append the name of the class instance (card) to a list
as I create it.\
\
While writing my UML, I learned that the __getitem__ dunder can be used by 
doing instance = class and then a separate line calling instance[index] where the
index is a parameter of the __getitem__ dunder function. In our program we will
use this to get a specific option from our menu options list.\
\
In Menu.py, there are calls to the chCommand function and the szDescription
function, but those only exist in MenuOption.py, so I'll have to import that class.
I might just end up combining Menu.py and MenuOption.py because I don't really
see the need for them to be separate.\
\
There's a confusing part in the initializer of RandNumberSet.py where we set the
nMax to be the greater of the given nMax and 2 x N^2. This is a default option in
case the number the user specified isn't high enough to be in the right range. What
happens if the user gives too high of a number? I might have to change this code to
account for that. It also append to the segments list a list of number between
low and high + 1. I went through it in the REPL and I think this will cause overlap
between the different columns of the Bingo card, especially because the new low is the
same as the old high, and both the high and low get included in the appended list of
numbers. I might change this as well. In this same RandNumberSet class, the __getitem__
dunder produces a row of Bingo numbers, not the column, as a list. You can specify which
row you want when you call it through n, and n will be the index spot, not the number of
the row. The shuffle function is the way that the segments for the columns are randomly
chosen without repeats. It just simplifies it all.\
\
I don't understand the use of __get_str and __get_int in UserInterface.py. They
seem to just be there to validate whether the user input is valid or not but I don't
see the point of this when the functions do this as they collect input.\
\
I think one of the harder parts for me will be to figure out how to copy the output into
a file. I also see myself struggling with implementing the MenuOptions class in the right
spot because I don't see a great option of where to put it.


## Phase 1: System Analysis *(10%)*

**Deliver:**

* List all of the data that is used by the program, making note of where it comes from.
* Explain what form the output will take.
* Describe what algorithms and formulae will be used (but don't write them yet).

__*RandNumberSet:*__ will be initialized with a number of rows and columns N and the
maximum number M allowed on the Bingo card. If the size of the card is too small or too
large, set it to the closest number within the range using MIN_SIZE and MAX_SIZE.
If the largest given number for the Bingo card values is too small, set it to the minimum,
which is 2xNxN. We will have a list of segments used to hold all the possible numbers that
could exist for each column of the Bingo card. We find the size of the segment by
using integer division and finding the remainder. We will split the maximum number
into N groups and then out of those N groups, remainder number of them will get an 
extra value. Then we use these sizes of segments to count up from 1. Each segment
will contain a list of a range of numbers of the appropriate size. The len dunder
will output the length or size of the Bingo card, so the value of N. The getitem
dunder will return a certain row of the Bingo card using an index parameter that
grabs that index from each of the segment lists. The shuffle function will shuffle
all the numbers in each segment so that you can have randomly generated Bingo cards
in your deck. It also resets the rowPosition to 0. The next_row method returns a
list of the numbers in the next row of the Bingo card and then it sets the rowPosition
to the next row. If the rowPosition is out of range, it doesn't return anything.
The str dunder returns all of the numbers on the card. It returns a lists of lists
separated by a new line character.\
\
__*Card:*__ This class lets us know that the letter labels for the Bingo cards use
"BINGODARLYZEMPUX". We will initialize the class with an ID number. We will do this
when we build our deck, and we'll pass in the index. I'll make a private variable
self.__idnum from the idnum parameter. I'll make another private variable self.__nSize
from the ns parameter than represents the size of the Bingo card, so the N value.
The id method will return self.__idnum. The number_at method will use the getitem 
dunder from RandNumberSet, which returns all the numbers in a certain line of the
Bingo card. We will use the row and column parameters in the number_at method to 
pass the row parameter to the getitem dunder and the column parameter will be the index. 
The str dunder will return the image of the Bingo card. We'll have to check if the
card is even- or odd-sized before we do this to determine whether we'll have a free
space. Then I'll use the format outlined in the instructions. When we print the
board we'll have to use the previous methods we just made and "BINGODARLYZEMPUX"
to figure out what we should be printing.\
\
__*Deck:*__ The deck is created in UserInterface.py
which is where we will ask the user for information. The data from there will be
passed into the Deck class. The types of data we will get are card size, number of
cards, and maximum number. The len dunder will return the size of the deck, which 
is one of the pieces of data that the user is asked to input (num_cards). In the
initializer we'll want to check that self.__num_cards is within the range 2 and 8192.
We'll do this the same way we checked that the size was within its range in
RandNumberSet with a set max and min value. After I make RandNumberSet the parent
class of Card, I will be able to pass the parameters of Deck to a Card instance.
I will make num_cards instances that are held together in a list. I will initialize
this list as a range of numbers from 1 to num_cards. Then I will make a for loop
that makes list[index] = Card() instance. \
\
__*MenuOption:*__ I will make this the parent class of Menu. It initializes a
command based on the input from the user given to it by UserInterface.py. If the
input is an empty string, give them question marks to let the user know. If they
give multiple inputs, only accept the first. If the command description input from
the user is empty, give them question marks again. The chCommand method returns the
letter of a command. The szDescription method returns the description of that
command. The str dunder will return both the letter and description of the command.\
\
__*Menu:*__ When this class is initialized, it will be labeled with a header, which
is one of its parameters. It will also have any empty list ready to be filled with
menu options. Therefore, the menu can be customized with its name and its commands.
There's an iadd dunder which is how you can add commands to the menu. The 
getitem dunder is how you look at certain commands from the menu one at a time using
an index. The len dunder will give you the number of commands in the menu. We
have a method to check whether the command that the user inputted to be performed
is valid by checking it with the command list in the menu. Our prompt method is 
uses the chCommand method and the szDescription method from MenuOption.py and prints
them for the user to see. Once it prints all of them, it prints an input statement
asking for a command and relists all the chCommands that are options. Then we use
our previously defined bIsValidCommand from earlier in the Menu class to determine
whether it is valid. If it is, we return the command to the value of commmand in 
UserInterface.py. If it isn't, we repeat the process.\
\
__*UserInterface:*__ This class initializes with an empty deck variable self.__m_currentDeck
and a Main Menu with two commands added to it right away. The run method will print
a welcome message and then move into the prompt method from the Menu class. This
will print the things we previously outlined for the Main menu. If the returned
command is C, we will be creating a deck in a method to come. If the returned
command is X, we will exit the program. I think I will have to add to this method
to make other functionalities of the program work. I'll add self.__deck_menu to
it. Because that method does the same thing as run but with different options. These
options will print a card, print the whole deck, save the deck to a file, and 
return to the main menu. The __get_str method will prompt the user for a value then 
check that the input isn't an empty string. The __get_int method is similar because
it checks for empty input too. It also ensures that the integer inputted is a number
and is within the range specified by the parameters. The __create_deck method creates
an instance of Deck. The __print_card method asks the user for which card they
want to print and prints it. The __save_deck method will write the string for 
printing the deck into a file.


## Phase 2: Design *(30%)*

**Deliver:**

* Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain the purpose, inputs and outputs.
* Pseudocode that captures how each function works.
    * Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
    * Explain what happens in the face of good and bad input.
    * Write a few specific examples that occurred to you.

```python
    # in RandNumberSet, most of it is already done for us
    # I just have to fix a bug near the bottom of the initializer
    def __init__(self, nSize, nMax):	         	  
        self.__m_nSize = nSize  	         	  
        if self.__m_nSize < RandNumberSet.MIN_SIZE:  	         	  
            self.__m_nSize = RandNumberSet.MIN_SIZE  	         	  

        if self.__m_nSize > RandNumberSet.MAX_SIZE:  	         	  
            self.__m_nSize = RandNumberSet.MAX_SIZE  	         	  

        self.__m_nMax = max(nMax, self.__m_nSize * self.__m_nSize * 2)  	         	  
        self.__m_nRowPos = 0  	         	  

        segments = []  	         	  
        segment_size = nMax // self.__m_nSize  # n.b. `//` operator means "integer division"  	         	  
        remainder = nMax % self.__m_nSize  	         	  
        low = 1  	         	  
        for segment in range(1, self.__m_nSize + 1):  	         	  
            high = low + segment_size  	         	  
            if segment <= remainder:  	         	  
                high += 1  	      
########### the line below is the only one getting changed
            segments.append(list(range(low, high)))  	         	  
            low = high  	         	  
        self.segments = segments
```
```python
class Card():  	         	  
    COLUMN_NAMES = list("BINGODARLYZEMPUX")  	         	  

    def __init__(self, idnum, ns):  	         	  
        """  	         	  
        Initialize a Bingo! card  	         	  
        """  	         	  
        self.__idnum = idnum
        self.__numberSet = ns

    def id(self):  	         	  
        """  	         	  
        Return an integer: the ID number of the card  	         	  
        """  	         	  
        return self.__idnum 	         	  

    def number_at(self, row, col):  	         	  
        """  	         	  
        Return an integer or a string: the value in the Bingo square at (row, col)  	         	  
        """  	         	  
        return self[row][col]  # uses RandNumberSet    	  

    def __len__(self):  	         	  
        """  	         	  
        Return an integer: the length of one dimension of the card.  	         	  
        For a 3x3 card return 3, for a 5x5 return 5, etc.  	         	  
        """  	         	  
        return len(self.__numberSet)       	  

    def __str__(self):  	         	  
        """  	         	  
        Return a string: a neatly formatted, square bingo card  	         	  
        """  	         	  
        print("Card #", self.__idnum)
        for n in range(self.__nSize):
            # print(format("%6s", "   {COLUMN_NAMES[n]}"), end="")
            print COLUMN_NAMES[n] in 6 spaces
            print("\n")
            printBoardLine(self.__nSize)
        for row in range(self.__nSize):
            for col in range(self.__nSize):
                print("|", end="")
                if self.__nSize % 2 == 1 and col == self.__nSize//2 + 1 and row == self.__nSize/2 + 1:
                    print("FREE!")
                else:
                    print(number_at(row,col) in 3 spaces, end="  ")
            print("|", end="")
            printBoardLine(self.__nSize)
                
        # i might want to set up one of the return f statements like in Assn2
                
        '''return f"""
        Card #{self.__idnum}
          {COLUMN_NAMES[0]}
        """'''
                
    
def printBoardLine(width):
    for i in range(width):
        print("+-----", end="")
    print("+")
```
```python
from Card import Card  	         	  
from RandNumberSet import RandNumberSet  	         	  

class Deck():  	         	  
    def __init__(self, card_size, num_cards, max_num):  	         	  
        """  	         	  
        Deck constructor  	         	  
        """ 
        self.__card_size = card_size
        self.__num_cards = num_cards
        self.__cards = list(1, max_num)
        
        for id in range(max_num):
            self.__cards[id] = Card(id, card_size, RandNumberSet(card_size, max_num))    
            self.__cards[id].shuffle()

    def __len__(self):  	         	  
        """  	         	  
        Return an integer: the number of cards in this deck  	         	  
        """  	         	  
        return len(self.__cards)     	  

    def card(self, n):  	         	  
        """  	         	  
        Retrieve Card N from the deck  	         	  
        """  	         	  
        return self.__cards[n]	         	  

    def __str__(self):  	         	  
        """  	         	  
        Return None: Display the entire Deck as a string  	         	  
        """  	         	  
        for i in range(len(self.__cards)):
            # this code won't actually work!! just pseudocode for an idea
            return self.__cards[i]
```
```python
from math import floor  	         	  

import Deck  	         	  
from Menu import Menu  	         	  
from MenuOption import MenuOption  	         	  


class UserInterface():  	         	  
    """  	         	  
    Provide the UserInterface for the program, which consists of the Main menu and the Deck menu  	         	  

    Also provides methods for accepting and validating user input  	         	  
    """  	         	  

    def __init__(self):  	         	  
        self.__m_currentDeck = None  	         	  
        self.__m_menu = Menu("Main")  	         	  
        self.__m_menu += MenuOption("C", "Create a new deck")  	         	  
        self.__m_menu += MenuOption("X", "Exit the program")  	         	  

    def run(self):  	         	  
        """  	         	  
        Return None: present the main menu to the user  	         	  

        Repeatedly prompt for a valid command until good input is given, or the program is exited  	         	  
        """  	         	  
        print("Welcome to the Bingo Deck Generator\n")  	         	  

        while True:  	         	  
            command = self.__m_menu.prompt()  	         	  
            if command.upper() == "C":  	         	  
                self.__create_deck()  
                # I don't actually know where I should put __deck_menu so it will run
                self.__deck_menu()
            elif command.upper() == "X":  	         	  
                break  	         	  

    def __deck_menu(self):  	         	  
        """  	         	  
        Return None  	         	  

        Present the deck menu to user until a valid selection is chosen  	         	  
        """  	         	  
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

    def __get_str(self, prompt):  	         	  
        """  	         	  
        Return a string: non-empty input entered by the user  	         	  

        Take a prompt string as input  	         	  
        Repeat the prompt until a non-empty string is provided  	         	  
        """  	         	  
        while True:
            value = input(prompt)
            if value != "":
                return value

    def __get_int(self, prompt, lo, hi):  	         	  
        """  	         	  
        Return an integer: validated integer input by user  	         	  

        Take a prompt string, low and high integers as input  	         	  
        Repeat the prompt until an integer that is in-range is provided  	         	  
        """  	         	  
        while True:
            value = input(prompt) 	
            if value.isnumeric() and lo <= int(value) <= hi:
                return int(value)

    def __create_deck(self):  	         	  
        """  	         	  
        Return None: Create a new Deck  	         	  

        The Deck is stored in self.__m_currentDeck  	         	  
        """  
        cardSize = self.__get_int("Enter your Bingo card size: ", 3, 16)
        numCards = self.__get_int("Enter number of cards in your deck: ", 2, 8192)
        maxNum = self.__get_int("Enter the maximum number allowed on your cards: ", 0, floor(3.9 * numCards * numCards))
        self.__m_currentDeck = Deck(cardSize, numCards, maxNum)	         	  

    def __print_card(self):  	         	  
        """  	         	  
        Return None: Print one Card from the Deck  	         	  

        Prompt user for a Card ID  	         	  
        """  	         	  
        cardId = self.__get_int("Number of desired card: ", 0, len(self.__m_currentDeck) - 1)
        print(self.__m_currentDeck.card(cardId))

    def __save_deck(self):  	         	  
        """  	         	  
        Return None: Save a Deck to a file  	         	  

        Prompt user for the name of file to write the entire Deck into  	         	  
        """  	         	  
        filename = self.__get_str("Name of file to write the Deck into: ")
        file = open(filename)
        file.write(self.__m_currentDeck)
        file.close()
```


## Phase 3: Implementation *(15%)*

**Deliver:**

*   (More or less) working code.
*   Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan

The str dunder was a pretty consistent struggle. I had to figure out how to return
a string where I would usually just put out some print statements. In Card I had
to make that switch and then return a string. In Deck I had to figure out how to
get the str dunder to accept the str dunder from Card so I could make a bigger string.
I ended up having to explicitly call the dunder because the regular way wasn't working.
I was having a hard time figuring out how the MenuOption methods were passed into Menu
but I figured it out. When you use the Menu dunder iadd, you append MenuOption objects
into Menu, which gives them the properties and accessbility to the methods in 
MenuOption. This is why when we call self[i], it refers to an instance of MenuOption
and can pull out its chCommand and szDescription.


## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

*   A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
*   Write your test cases in plain language such that a non-coder could run them and replicate your experience.

A huge issue I had was once I built my deck, when it printed it would print only
the last card for every card in the deck. I'm not sure exactly why this happened,
but I changed it so that my instance randomSet of RandNumberSet would be initialized
right before the set it produced was passed to Deck as a parameter. I also messed up when I set the max size.
I set it equal to floor(3.9 * the size of the deck squared) so it wouldn't let
me set the max size to more than like 16 when my deck size was 2. I fixed that pretty
quickly. The unit tests kept failing in testDeck and I couldn't get them to pass
so I went back to the instructions that said I could change them to fit my needs 
since they assume things about my code that may not technically be correct. Once
I did that, everything was good to go and my code was working great! Another bug
that happened was when I input an invalid text file for my deck to be saved to.
It crashed the program which wasn't supposed to happen so I set up some code to 
catch it just in case. Now if an invalid file is entered, the user will simply be
prompted for a different in hopes that it will open this time.


## Phase 5: Deployment *(5%)*

**Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 6: Maintenance

**Deliver:**

* Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
* Fill out the Assignment Reflection on Canvas.

My code for my nicely formatted bingo card is a bit sloppy. It was the only way I 
could figure to do it while keeping it dynamic enough for different sizes and a possible
free space. Most of it is pretty self-explanatory.\
There are some parts of the program that I had to take a leap of faith with. I spent
many hours studying the starter code and instructions so I could work with what I 
had instead of making it harder for myself. There are a couple of spots that seem like
shouldn't work where they do. For example, in Deck, I have to put randomSet inside
the for loop or it won't work. I couldn't explain to you why that is.\
If I had to fix a bug in a few months, I think I'd be able to find it very easily.
I know this program inside and out because I spent so long on my design and analysis
phases.\
My documentation for this assignment is a bit confusing because I wrote
it as I went along. I decide certain things about how it should work and then
switch later on as I understand better. My UML stays consistent, though. I should
make sense to me after a while because I know where to go to find the most
important parts, what are namely Phase 1 and Phase 2 with my thorough analysis
and pseudocode. \
It will be very easy to add new features due to the multi-class structure of the 
program. The purpose of this type of coding is to simplify and increase readability.
It also increases usage possibilities. \
My program should work with new updates of hardware, operating systems, and Python 
versions. I don't use any obscure libraries or techniques. They're all fairly simple,
just highly intermingled. 
