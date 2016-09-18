'''Remember, we used the % operator to replace the %s placeholders with the variables in parentheses.

name = "Mike"
print "Hello %s" % (name)
You need the same number of %s terms in a string as the number of variables in parentheses:

print "The %s who %s %s!" % ("Knights", "say", "Ni")
# This will print "The Knights who say Ni!"
Instructions
Now it's your turn! We have ___ in the code to show you what you need to change!

Inside the string, replace the three ___ with %s.
After the string but before the three variables, replace the final ___ with a %.
Hit Save & Submit Code.
Answer the questions in the console as they pop up! Type in your answer and hit Enter.'''


name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)
