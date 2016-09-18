'''Let's take a closer look at why you use len(string) and str(object), but dot notation (such as "String".upper()) for the rest.

lion = "roar"
len(lion)
lion.upper()
Methods that use dot notation only work with strings.

On the other hand, len() and str() can work on other data types.

Instructions
On line 3, call the len() function with the argument ministry.
On line 4, invoke the ministry's .upper() function.'''





ministry = "The Ministry of Silly Walks"

print len(ministry)
print ministry .upper()
