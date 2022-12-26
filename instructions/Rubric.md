# CS 1440 Assignment 3 Rubric

| Points | Criteria
|:------:|--------------------------------------------------------------------------------
|  25    | Software Development Plan is comprehensive and well-written. Follows DuckieCorp project conventions.
|  5     | Signature file is complete
|  10    | Design Phase UML fully meets requirements and describes starter code according to standards covered in class
|  5     | Design Phase User Manual is written to a level of detail appropriate for an end user<br/>Manual adequately explains how to run the program
|  10    | Design Phase Peer Reviews<br/>2 design reviews of at least 250 words each are written for study buddies<br/>Any reviews received from study buddies are also included
|  5     | Commits marking the end of the System Analysis and Design phases are tagged<br/>These tags are pushed to GitLab so the grader can see them
|  20    | Final Submission Implementation <br/> The program meets requirements
|  5     | Final Submission User Manual is written to a level of detail appropriate for an end user <br/> Accurately describes the UI of the final product
|  10    | Final Submission UML matches final submission implementation and is written according to standards covered in class.
|  15    | All supplied Unit Tests pass <br/> Unit Tests are meaningful <br/> No trivial unit tests are present <br/> Suitable replacements are provided if your design invalidates the supplied tests

**Total points: 110**


## Penalties

*Review "How To Submit Assignments" on Canvas (found under the DuckieCorp Employee Handbook Module) for more information on penalties and what we expect.*

***Penalties for this assignment***:

0.  **110 point penalty** if your program imports any modules **except**:
    *   `sys`
    *   `unittest`
    *   `random`
    *   `math`
    *   modules that are provided by the starter code
    *   or modules you wrote yourself
    *   This assignment is about the experience of solving this puzzle for yourself without leaning on code written by others, no matter how "real-world" it would be to do so.


***Penalties for all assignments***:

#### Project Layout
0. **10 point penalty** if the repository does not follow the Git Repository Naming Convention
1. **10 point penalty** if the submitted project is not a clone of the starter code repository.
2. **10 point penalty** if there is an omission of required files and directories (missing, renamed, or moved from their expected location)
3. **10 point penalty** if there are forbidden files and directories in the submission
4. **10 point penalty** if there is no `.gitignore` file (whether it is missing or corrupted)
5. **Late Penalty**:
    *   \<24hrs late = -25% total points
    *   \>=24hrs & <48hrs = -50% total points
    *   \>=48hours = -100% total points


#### Modules and Functions
0. **10 point penalty** if a module fails to import due to misspelling or incorrect capitalization.
1. **10 point penalty** if the program attempts to import a module from the `src.` package; this is the result of a PyCharm misconfiguration.
2. **10 point penalty** `eval()` or a similar function is used by your program; use type constructor functions such as `int()` and `float()` instead


#### Files and Paths
0. **10 point penalty** if the program contains hard-coded paths or otherwise does not function when run from *any* CWD.  (Note: names of modules in `import` statements do not count as "hard-coded").
1. **10 point penalty** if one or more data files are not closed after being processed in *ordinary* situations.  In the event of an error your program will display an error message and immediately exit; in such cases you do not need to take special measures to close files because they will automatically be closed as your program exits.
2. **100% point penalty** if external programs are called upon to do the work
    - Do not use `os.system()`, `subprocess`, `pipes` or similar functions and libraries
    - Our customer has hired us to create a pure-Python solution, not a shell script that relies on external programs.


#### All Else
0. **Crashing Code Penalty**:
    * *It is your responsibility to test and ensure that your program works on the graders computer*
    *   Code that crashes and cannot be quickly & easily fixed by the grader will receive 0 points on the Implementation portion of the rubric
    *   Code that crashes and CAN be quickly & easily fixed by the grader (or crashes only some of the time) will receive at most 50% on the Implementation portion of the rubric
