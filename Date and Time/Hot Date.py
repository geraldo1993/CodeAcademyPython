'''What if we want to print today's date in the following format? mm/dd/yyyy. Let's use string substitution again!

from datetime import datetime
now = datetime.now()

print '%s-%s-%s' % (now.year, now.month, now.day)
# will print: 2014-02-19
Remember that the % operator will fill the %s placeholders in the string on the left with the strings in the parentheses on the right.

In the above example, we print 2014-02-19 (if today is February 19th, 2014), but you are going to print out 02/19/2014.

Instructions
Print the current date in the form of mm/dd/yyyy.

Change the string so that it uses a / character in between the %s placeholders instead of a - character.
Re-arrange the parameters to the right of the % operator so that you print now.month, then now.day, then now.year.'''



from datetime import datetime
now = datetime.now()

print '%s/%s/%s' % (now.year, now.month, now.day)
