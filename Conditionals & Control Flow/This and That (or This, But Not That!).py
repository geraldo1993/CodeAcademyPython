'''Boolean operators aren't just evaluated from left to right. Just like with arithmetic operators, there's an order of operations for boolean operators:

not is evaluated first;
and is evaluated next;
or is evaluated last.
For example, True or not False and False returns True. If this isn't clear, look at the Hint.

Parentheses () ensure your expressions are evaluated in the order you want. Anything in parentheses is evaluated as its own unit.

Instructions
Assign True or False as appropriate for bool_one through bool_five.

Set bool_one equal to the result of False or not True and True
Set bool_two equal to the result of False and not True or True
Set bool_three equal to the result of True and not (False or False)
Set bool_four equal to the result of not not True or False and not True
Set bool_five equal to the result of False or not (True and True)'''


bool_one = False or not True and True

bool_two = False and not True or True

bool_three = True and not (False or False)

bool_four = not not True or False and not True

bool_five = False or not (True and True)
