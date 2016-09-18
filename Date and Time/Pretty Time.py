'''Nice work! Let's do the same for the hour, minute, and second.

from datetime import datetime
now = datetime.now()

print now.hour
print now.minute
print now.second
In the above example, we just printed the current hour, then the current minute, then the current second.

We can again use the variable now to print the time.

Instructions
Similar to the last exercise, print the current time in the pretty form of hh:mm:ss.

Change the string that you are printing so that you have a : character in between the %s placeholders.
Change the three things that you are printing from month, day, and year to now.hour, now.minute, and now.second.'''

from datetime import datetime
now = datetime.now()

print '%s:%s:%s' % (now.year, now.month, now.day)
