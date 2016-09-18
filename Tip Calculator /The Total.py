'''Now that meal has the cost of the food plus tax, let's introduce on line 8 a new variable, total, equal to the new meal + meal * tip.

The code on line 10 formats and prints to the console the value of total with exactly two numbers after the decimal. (We'll learn about string formatting, the console, and print in Unit 2!)

Instructions
Assign the variable total to the sum of meal + meal * tip on line 8. Now you have the total cost of your meal!'''




# Assign the variable total on line 8!

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total=meal+meal*tip

print("%.2f" % total)
