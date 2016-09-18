'''We've managed to print the date and time separately in a very pretty fashion. Let's combine the two!

from datetime import datetime
now = datetime.now()

print '%s/%s/%s' % (now.month, now.day, now.year)
print '%s:%s:%s' % (now.hour, now.minute, now.second)
The example above will print out the date, then on a separate line it will print the time.

Let's print them all on the same line in a single print statement!

Instructions
Print the date and time together in the form: mm/dd/yyyy hh:mm:ss.

To start, change the format string to the left of the % operator.

Ensure that it has 6 %s placeholders.
Put slashes and colons and a space between the placeholders so that they fit the format above.

Then, change the variables in the parentheses to the right of the % operator.

Place the variables so that now.month, now.day, now.year are before now.hour, now.minute, now.second. Make sure that there is a ( before the six and a ) after them.'''


from datetime import datetime
now = datetime.now()

print '%s/%s/%s %s:%s:%s' % (now.year, now.month, now.day ,now.hour,now.minute,now.second)

