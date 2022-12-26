# Reviews You Gave

### Ally Hassett
### Ben Hamner

It's good that you specified that Deck uses Card and RandNumberSet, because Card
doesn't use RandNumberSet, though it's a bit deceptive. COLUMN_NAMES in Card should
be a list, not str[]. That's more like the Java definition. Also, ns in the parameters
of the init dunder in Card should be a list as well, not an integer. It should also
return void or none, not return self. It's also private, not public. The segments
variable in RandNumberSet should also be a list type. You forgot the init dunder in
RandNumberSet as well. The options variable in Menu should be a list type. Check the 
return type of the init dunder of Menu and UserInterface as well. The prompt method will return a string
that is the command. Make sure to include the init dunder in MenuOption. The get_int
method in UserInterface should return an integer, not a string. Overall, your UML is very
readable and you identified the visibility of every variable and method. It might be
a good idea to double check what you define as public and private though, because your
init dunders are all identified as public but they should be private. There are a few 
misunderstandings between what the return types of methods are. When you identify the list
type variables as int[][] or int[], it's not really much of an issue. I also don't
understand the difference between "contains" and "uses". You should define it somewhere
on the UML so readers understand it more. I like how you put UserInterface the top
because it makes it very easy to tell what the most main class is. I also like how 
MenuOption is at the bottom, because both Menu and UserInterface use it, so it's
the bottommost and lowest level class.

------------------------------------------------------------

### Ally Hassett
### Nathan Taylor

This is very aesthetic and I like it. Your RandNumberSet box is missing quite a
few variables. You should add the class variables (the ones that start with self). It
might just be that you didn't add any variables except the one provided in the
starter code. Also you should provide the types of variables they are, like boolean,
integer, string, an object (you could add with object class it is or not), list,
void, etc. You should also check on whether your methods are public or private. For
example, your init dunders in RandNumberSet, Deck, Card, UserInterface, Menu, and 
MenuOption should be private. You have them labeled as public. The same way you
should add the variable type to the variables in the top box of the class box
things, you should add the return type of the methods. A lot of them won't return 
anything so you'd label it as void or none. There are also a lot of missing variables.
I don't know how you altered the starter code, but most likely you will still have
some of the original variables. In UserInterface you should at least have m_currentDeck
and m_menu. Also in your MenuOption, your method privacy are all switched up. + is for
public and - is for private. chCommand should be public and szDescription should
be public since we use them in Menu. I really like the colors on your UML and
it's easy to read and understand your arrow labels. You could rearrange the boxes
so it matches the flow of the program a little closer, but that's all I would
change. Good job!

------------------------------------------------------------

# Reviews You Received

### Review from Ben Hamner

I like that you put the classes with the complete name for accuracy.
It's good that you put the classes in a way that is clear, and it
visualized the flow that each class interacts with the other. 
It's good that you specified the way that each class uses the other. 
For example UserInterface uses Deck but not the other way around.  
Just be sure to use dotted lines for dependencies and solid lines for
associations.  I don't know if it required or not but you can put text
in next to each line to describe how the classes interact with eachother.
These are some of the requirements detailed in the instructions:
* Dependencies and associations are correctly distinguished
* Navigability of associations is correct
* Multiplicity constraints are present on all associations

make sure that you include the multiplicities for each class.  I just
realized that I forgot to do that on mine.  I really like how clear you
made each item within the classes.  Each of the methods appear to have the
correct visibility whether that be private or public.  Even though python
doesn't have very much security concerning the visiblity of variables or
methods.  There are a few methods in the RandNumberSet() that don't have
any return types.  For example __len__(), __getitem__(), shuffle(), next_row().
I honestly don't really understand completely how to know if something is private
or public.  I might not be a good source of information regarding how or when 
to use a public variable/method for a given class.  Other than those things,
it looks great I love the yellow color choice just beautiful.

### Review from Nathan Taylor

Dear Ally, Thank you for taking the time to review my UML diagram and 
sending me yours. Your diagram looks pretty good. You have all of the classes 
represented along with all the variables and methods within each class. However, 
I did notice that you have all of your __init__ methods labeled as private 
methods. I could be wrong, but I thought that all dunders are public. That
would be something you would want to double check though. Take this with 
a grain of salt. You do have all your other dunder methods labeled as public
methods though, so good job with that. You did put all methods that begin 
with __ but are not dunders as private, which is correct, but you left the 
__ on the method name here. I do not think it is technically wrong, but it 
could look a but nicer if you deleted the __ from the method name and just had
the private method indicator thing before it. Putting both of them just seems to
me like it is redundant. I also noticed that for the methods that do not return
anything you put the return type as void. This is another thing that I so not 
think is technically wrong, but I think None would be better because in the 
actual method you wouldn’t type “Return void”, you’d probably type “Return None”
or just no return statement. This is just a small side note that is not really
relevant to how good your actual UMl diagram is, but I like the color you 
chose for the background. It is a very nice and soothing yellow. Overall it looks really good.

