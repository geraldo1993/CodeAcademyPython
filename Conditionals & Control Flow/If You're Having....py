'''Let's get some practice with if statements. Remember, the syntax looks like this:

if some_function():
    # block line one
    # block line two
    # et cetera
Looking at the example above, in the event that some_function() returns True, then the indented block of code after it will be executed. In the event that it returns False, then the indented block will be skipped.

Also, make sure you notice the colons at the end of the if statement. We've added them for you, but they're important.

Instructions
In the editor you'll see two functions. Don't worry about anything unfamiliar. We'll explain soon enough.

Replace the underline on line 2 with an expression that returns True.
Replace the underline on line 6 with an expression that returns True.
If you do it successfully, then both "Success #1" and "Success #2" are printed.'''





def using_control_once():
    if 2+2==4:
        return "Success #1"

def using_control_again():
    if (5*2)==10:
        return "Success #2"

print using_control_once()
print using_control_again()
