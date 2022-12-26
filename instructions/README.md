# CS 1440 Assignment 3 Instructions

## Important!
**I have instructed the CS Coaches to _not_ help you write code for this assignment until you have completed the Design phase and tagged your repository `designed`.  Don't even think about writing code until you have carefully considered the design.  Countless software projects have gone awry because the design phase was neglected.  Don't become a statistic - think first, code after.**


## Description

In this assignment, you will design classes that work together to help users generate a deck of Bingo cards.

Bingo is a simple game where players try to mark all numbers in a row or column or along one of the two diagonals of a Bingo card. The rules of the game of actually not important for this project, as you are only making a program to print the cards.

This program is only partly complete: the finished program will allow a user to create a deck, print a card from the current deck, display the entire deck, or save the entire deck as a text file.  Unit tests are provided, though at this early stage many will fail because the program is still incomplete.



## Previous Semester Assignment Statistics

Statistic                        | Value
--------------------------------:|:---------------
Average Hours Spent              | 10.07
Average Score % (Grade)          | 85.53% (B)
% students thought this was Easy | 17.65%
... Medium                       | 58.82%
... Hard                         | 21.57%
... Too Hard/Did not complete    | 1.96%



## Part 0: Requirements Specification and System Analysis

0.  Carefully study the **Program Requirements** section below
1.  Carefully study the starter code
    *   Seriously, read it and take notes!
2.  Create a UML class diagram that describes the starter code as it is given
    *   Put `Phase-0-UML` in this file's name
    *   **Do not** include these features
        *   Unit tests (this includes the file `src/runTests.py`)
        *   Files that don't define classes (e.g. `src/bingo.py`)
        *   Local variables used inside of methods
        *   The `self` parameter that is *always* passed to every method (it just takes up space on your diagram)
    *   **Do** include these features
        *   Class initializers (a.k.a. constructors)
            *   You can call this `__init__` or name it for the class (preferred)
        *   Dunders (BTW these have public visibility, mark with `+`)
        *   Methods that have already been written for you
        *   Methods that are not yet implemented (i.e. contain only the `pass` statement)
        *   Data members (variables whose names begin with `self.`)
        *   Class static data members (e.g. `Card.COLUMN_NAMES`)
    *   Write phases 0 and 1 of the Software Development Plan in tandem with this draft of the UML class diagram
    *   The diagram should match the starter code as well as your plan up to this point
    *   At this stage your UML class diagram does not need to use *all* of the UML concepts explained in class
        *   At minimum, all classes, methods and data members should be represented
        *   Relationships between classes may be modeled as dependencies (dashed lines with an open-arrow pointing toward the *depended on* class)
    *   Save your UML class diagrams as images (PNG or PDF are preferred) under the `doc/` directory
3.  Give the final commit of the System Analysis phase the tag `analysis`
    *   Explicitly push this tag to GitLab
    *   ```
        $ git tag analysis
        $ git push origin analysis
        ```
    *   If you make a mistake or need help with this tag, refer to the document `Using_Git/Intermediate_Git.md` in the Lecture Notes repository on Gitlab.
4.  Verify that your diagrams are legible by viewing them in your browser after pushing to GitLab


## Part 1: The Design Phase

1.  Create a first draft of a **User Manual** describing the expected user interface (UI)
    *   You don't quite have a working UI yet, so this will be your best guess at what using the program will be like
    *   The UI may change as you write code, but you should strive to make the design described by your manual
2.  Create a new UML class diagram when you begin phase 2 of the Software Development Plan
    *   Put `Phase-2-UML` in this file's name
    *   You are not limited to using only what is provided in the starter code
        *   You may devise new classes, methods and data members to satisfy the customer's requirements; include these new components on this draft
        *   You may also choose to remove elements from the design I provided; that's fine as long as it is **documented**
3.  Review the design phase UML diagrams of at least **two** study buddies
    *   Write a **250-word** peer review for each study buddy
    *   Save a copy of your reviews in `doc/Reviews.md`
    *   Send a copy of your review to your study buddies so they can improve their designs
4.  Share your design phase UML diagram with your study buddies
    *   Receive copies of your study buddies' reviews of your diagram
    *   Paste these reviews into `doc/Reviews.md`
5.  Give the final commit of the design phase the tag `designed`
    *   Explicitly push this tag to GitLab
    *   ```
        $ git tag designed
        $ git push origin designed
        ```
    *   If you make a mistake or need help with this tag, refer to `Using_Git/Intermediate_Git.md` in the Lecture Notes repository on GitLab.

At this point your repository will look like this:

```
|-- README.md
|-- doc
|   |-- Plan.md
|   |-- Signature.md
|   |-- Manual.md
|   |-- Phase-0-UML.png
|   |-- Phase-2-UML.png
|   `-- Reviews.md
|-- instructions
|   |-- Hints.md
|   |-- README.md
|   |-- Rubric.md
|   `-- examples
`-- src
    |-- bingo.py
    |-- Card.py
    |-- Deck.py
    |-- MenuOption.py
    |-- Menu.py
    |-- RandNumberSet.py
    |-- README.md
    |-- runTests.py
    |-- Testing
    |   |-- __init__.py
    |   |-- testCard.py
    |   |-- testDeck.py
    |   |-- testMenu.py
    |   `-- testRandNumberSet.py
    `-- UserInterface.py
```


### Tips for writing a User Manual

The User Manual describes only the user interface of the program.  The target audience for the manual is somebody with a little familiarity with computers and no knowledge of the Python programming language.

The manual should answer such questions as

0. How to run the program
1. What menus will the user see
2. What responses should the user give in response to those menus
3. How to perform the basic operations of the program (in our case, how to create a deck, how to print cards in the deck, how to save a deck to a file, how to quit the program)
4. What error messages the user may expect, and how to recover from mistakes

You may assume that your user already knows how to open a terminal and navigate to the project directory.

The User Manual differs from the Software Development Plan in that it should *not* include details about *how* the program works.  The manual does not need to describe the algorithms and data structures used by the program in order to guide a user in running it.


### Tips for drawing UML class diagrams

You may draw your UML class diagram using any software you prefer.  A simple tool that I recommend is [Diagrams.net](https://app.diagrams.net/)

0.  Open the website
1.  Click "Create New Diagram"
2.  Select the "Basic" "Blank Diagram" - don't use one of the pre-defined UML templates
3.  Find the UML section in the accordion list on the left-hand side of the screen

There are multiple shapes available with names like `Class`, `Class 2`, `Class 5`, etc.  Make sure that the classes appearing on your diagram have 3 sections as described in our lectures.

As you implement your design in Python code in the latter half of the assignment you will undoubtedly encounter problems you hadn't foreseen.  Update your UML diagram, User Manual, and Software Design Plan to match your code as your design changes.


## Part 2: Completing the Implementation and Testing

Armed with a clear design, you can now write Python code that realizes your vision.

### Important!
**I have instructed the CS Coaches to _not_ help you write code for this assignment until you have completed the Design phase and tagged your repository `designed`.  Don't even think about writing code until you have carefully considered the design.  Countless software projects have gone awry because the design phase was neglected.  Don't become a statistic - think first, code after.**

0.  Translate your design into code
    -   Meet all program requirements outlined below
    -   Manually verify that your program performs correctly
    -   Ensure that all Unit Tests pass
1.  It is normal for your design to evolve as you put it into code and test it
    -   Make new drafts of your UML class diagram and User Manual as things change
    -   Continue to update your software development plan
2.  At this stage of the project, your UML class diagram *should* include all of the UML concepts explained in class
    *   Specifically, we are looking for these features:
        *   All classes are present in the diagram
        *   All data members and methods are present and correctly named
        *   Data types of data members, methods and parameters are noted
        *   Dependencies and associations are correctly distinguished
        *   Navigability of associations is correct
        *   Multiplicity constraints are present on all associations
    *   Files that contain Unit Tests **do not belong on the UML class diagram**
    *   Files that do not define classes  **do not belong on the UML class diagram**


## Requirements

### User Interface

0.  DuckieCorp's C++ team completed the `Menu` and `MenuOption` classes before the project was turned over to you
    *   They designed the `UserInterface` class and implemented only part of it
    *   You will notice some bits of C++ style showing through, especially in the names of variables and methods
    *   This naming style is called [Hungarian Notation](https://en.wikipedia.org/wiki/Hungarian_notation)
    *   You can change it if you don't like how it looks, but be careful that you don't add new bugs into otherwise working code!
1.  C++ enforces the privacy of methods and data members within classes
    *   Python has privacy, too, but it's not nearly as strict as languages like C++ and Java
    *   Python variables and methods whose names begin with double underscores are *private*
2.  Follow these general UI principles in this project:
    *   Prompts should be repeated until the user provides valid input
    *   Case doesn't matter; *upper* case is just as valid as *lower* case



### Bingo Cards

0.  Every Card has a unique integer identifier
    *   This number can be the same as its position within its Deck
1.  A Bingo Card is an `N x N` grid, where `N` is the size of the card
    *   The typical size is 5x5, but we'll allow cards to vary in size from 3x3 to 16x16.
2.  Numbers on Cards are drawn from the set of integers `[1 .. M]` (inclusive)
    *   `M` is the maximum number that may appear in a Deck, its value depends on the size of the Card
    *   `M` is chosen by the user from the range `[2*N*N .. floor(3.9*N*N)]` (inclusive).
    *   A Bingo number *cannot* appear on the same Card more than once
    *   A Bingo number *can* appear on multiple cards in the same Deck
3.  The columns on a traditional 5x5 Bingo card are named `B`, `I`, `N`, `G`, and `O`
    *   This naming scheme has been extended to accommodate cards with up to 16 columns such that each column has a unique name
    *   Numbers in each column are drawn from `N` non-overlapping subsets of `[1 .. M]`, with values increasing column-wise from left to right
        *   On a 5x5 card, numbers in column `B` are drawn from the first 1/5th of numbers starting from `1`, column `I` gets the next 1/5th of numbers, and so on
        *   For a 3x3 card, numbers in column `B` are drawn from the first 1/3rd of numbers, column `I` gets the next 1/3rd of numbers, and column `N` gets the last 1/3rd
        *   This requirement was already fulfilled by the C++ team in the `RandNumberSet` class
        *   **However, one of the unit tests indicates that `RandNumberSet` produces duplicate numbers.  You should look into this bug.**
4.  Odd-sized cards have a **FREE!** square in the center
    *   **Free!** squares contain the string `"FREE!"` instead of an integer
    *   Even-sized cards don't have a center square and, thus, no **FREE!** square
5.  Once generated, a Card's appearance does not change
    *   If a Card is displayed multiple times, it's appearance is identical each time


### Decks of Bingo Cards

0.  The number of Bingo cards in a Deck is chosen by the user from the range `[2 .. 8192]` (inclusive).
1.  The `Deck` class must have the following capabilities:
    -   A method to print a specific card in the deck to the screen
    -   A method to print whole deck to the screen
    -   A method to write an entire deck to a file named by the user
2.  If you don't change the method definitions already provided for you in `Deck.py`, you should not have to change `UserInterface.py`
    *   You may add new methods and attributes to `Deck.py` as you see fit.
3.  Your solution may contain other classes besides `Deck`. In fact, it should!  If you try to put all the functionality in the `Deck` class your solution will most likely have a poor design. Use the overview given above to identify other meaningful classes.
4.  The deck should be able to retrieve a card given the identifier, so the user can print just that card to the screen.
    *   After a Deck has been created, a card that is displayed multiple times appears identical each time.
5.  When a new deck is created the previous Deck is lost

6.  When printing all a deck's cards to the screen or to a file, you may simply print every card, one after the other.
7.  This program uses interactive menus and prompts to gather user input.
    *   This program *does not* make use of command-line arguments
    *   Menu options are **case-insensitive**
        *   Note that the starter code displays *upper* case letters for its menus, even though it also accepts *lower* case input
        *   For consistency's sake, keep to this convention!
    *   Prompts asking the user for numeric *must* display the range of numbers that are accepted
    *   Validate *all* user input.  Ensure that numeric input is entered as integers
    *   Display helpful and appropriate messages to remind the user what kind of input is expected
    *   Continue to redisplay the prompt until valid data is provided
        *   Do not return to the previous menu or exit the program when invalid data is given
        *   Take special care that your program does not get into a bad state when bad data is input by the user; your program should be **robust**
8.  The program *must not* construct any cards if the user-supplied card size, number of cards, or maximum of Bingo numbers is invalid


### Formatting Output

0.  The Card's ID number is printed first
1.  The name of each column is centered above its cell
2.  Columns are separated by pipe characters `|`
3.  Rows are bounded by a line of the form `+-----+-----+` that is as wide as the entire Card
    *   There is one boundary line at the top and bottom of every card
4.  Cell contents are centered in a field 5 characters wide
    *   The widest value that can appear in a Card is the string `"FREE!"`
5.  The appearance of Cards is always the same, regardless of whether they are printed to the screen or written to a file

When a card is printed to the screen or to a file, it should be formatted *exactly* like these specimens:

**Odd-sized Card**

```
Card #62
   B     I     N     G     O
+-----+-----+-----+-----+-----+
| 10  | 17  | 35  | 50  | 64  |
+-----+-----+-----+-----+-----+
| 15  | 19  | 44  | 56  | 70  |
+-----+-----+-----+-----+-----+
|  8  | 30  |FREE!| 55  | 63  |
+-----+-----+-----+-----+-----+
| 11  | 26  | 32  | 59  | 67  |
+-----+-----+-----+-----+-----+
|  1  | 23  | 45  | 52  | 62  |
+-----+-----+-----+-----+-----+
```

**Even-sized Card:**

```
Card #10
   B     I     N     G
+-----+-----+-----+-----+
|  8  | 16  | 20  | 27  |
+-----+-----+-----+-----+
|  1  |  9  | 22  | 31  |
+-----+-----+-----+-----+
|  3  | 13  | 19  | 29  |
+-----+-----+-----+-----+
|  7  | 14  | 24  | 26  |
+-----+-----+-----+-----+
```

Examples of every size of Card are found under the [examples](./examples/) directory.


### Test-Driven Development

An important part of this assignment is to learn about unit tests and to gain experience approaching a problem through the Test-Driven Development methodology.  Writing your program to comply with the provided unit tests is meant to guide you toward a correct and robust solution, and is worth a large proportion of the points on this assignment.

However, you are given latitude in how your solution is structured and are free to add, remove, or refactor classes to meet the design you crafted in UML.  It is not intended for you to take advantage of this latitude in order to avoid unit tests.

As you craft your solution, please keep the following guidelines in mind:

*   The unit tests I provide make some assumptions about the way your code works
    *   My assumptions should not be seen as a "hint" to guide you to the "right way" of writing this program
    *   If your code does not fit my tests, change the tests to match your implementation
        *   If a unit test fails because you renamed a class, method or data member, update the unit test accordingly
        *   If a unit test fails because you removed a class, method or data member, from your design, you must _replace_ that unit test with another non-trivial unit test
        *   If a unit test fails because you moved a piece of functionality from one class to another, move that unit test into the file corresponding to the new class
*   Do not create _trivial_ unit tests
    *   A trivial unit test unconditionally passes, and does not give any insight about your code
*   Do not delete unit tests just because they don't pass; find ways to make your code compatible with the unit test, or re-write the test
*   Do not change unit tests to become less strict or trivial; instead, figure out how to make your code more robust
*   Some of the unit tests can take a *really* long time to run
    *   If you can, seek to improve the performance of your code so that `src/runTests.py` can finish in less than one minute
    *   If you can't make the test run in under a minute, adjust the test parameters downward so the test is less thorough, but still comprehensive

_**TL;DR**_ You have been given 13 non-trivial unit tests.  Your final submission must contain _at least_  13 non-trivial unit tests
