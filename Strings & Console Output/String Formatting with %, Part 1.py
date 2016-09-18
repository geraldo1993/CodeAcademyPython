'''When you want to print a variable with a string, there is a better method than concatenating strings together.

name = "Mike"
print "Hello %s" % (name)
The % operator after a string is used to combine a string with variables. The % operator will replace a %s in the string with the string variable that comes after it.

Instructions
Take a look at the code in the editor. What do you think it'll do? Click Save & Submit when you think you know.'''



string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)
