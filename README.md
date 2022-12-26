# CS 1440 Assignment 3: Bingo! Design and Implementation

*   [Instructions](./instructions/README.md)
    *   [Output examples](./instructions/examples/)
*   [Rubric](./instructions/Rubric.md)
*   [Hints](./instructions/Hints.md)

Clone this repository and use it as a basis for your work.  Run each of these commands one-at-a-time, without the '$' (that represents your shell's prompt).  Be sure to replace the words `LAST`, `FIRST`, and `USERNAME` with your own names.

```
$ git clone git@gitlab.cs.usu.edu:erik.falor/cs1440-falor-erik-assn3 cs1440-LAST-FIRST-assn3
$ cd cs1440-LAST-FIRST-assn3
$ git remote rename origin old-origin
$ git remote add origin git@gitlab.cs.usu.edu:USERNAME/cs1440-LAST-FIRST-assn3.git
$ git push -u origin --all
```

## Important!
**I have instructed the CS Coaches to _not_ help you write code for this assignment until you have completed the Design phase and tagged your repository `designed`.  Don't even think about writing code until you have carefully considered the design.  Countless software projects have gone awry because the design phase was neglected.  Don't become a statistic - think first, code after.**


## Overview

For your next project at DuckieCorp you are tasked with writing an interactive Bingo card generator.  This project was started by our C++ team, but partway through the customer and the project manager decided that Python would be a better platform for this system.  I translated the partially-completed C++ program into Python before the project was assigned to you.  Some traces of the original C++ coding style are still evident.

You will create a complete *programming product* consisting of

*   A clean program that can be easily modified
*   Documentation (both technical and user-oriented)
*   Unit Tests

As you well know, creating a *programming product* can take up to 3x as much time as just making a simple program.  Plan for this and carefully manage your time so that you can meet the deadline.

## Objectives

*   Learn to design before you code
*   Write a users' manual at an appropriate level of detail
*   Study existing resources to identify requirements
    *   Read source code to identify which parts are already implemented
    *   Extract the customer's requirements from the specification
    *   Create UML Class diagrams from source code
*   Extend a software system with new classes and features
    *   Design classes in UML first, then in code later
    *   Implement code to achieve the design
    *   Validate that your program is "doing the right thing"
*   Support your implementation work with unit tests
    *   Design code to meet the test's specifications
    *   Create or modify tests as your design evolves
    *   Verify that your program is "doing the thing right"
