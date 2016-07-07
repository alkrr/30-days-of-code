"""
Task 
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), 
and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

Input Format

There are  lines of numeric input: 
The first line has a double,  (the cost of the meal before tax and tip). 
The second line has an integer,  (the percentage of  being added as tip). 
The third line has an integer,  (the percentage of  being added as tax).

Output Format

Print The total meal cost is totalCost dollars., where  is the rounded integer result of the entire bill ( with added tax and tip).

"""

mealCost   = float(raw_input())
tipPercent = int(raw_input())
taxPercent = int(raw_input())

tipPaid = mealCost * (tipPercent / 100.0)
taxPaid = mealCost * (taxPercent / 100.0)

totalCost = int(round(mealCost + tipPaid + taxPaid))

print "The total meal cost is " + str(totalCost)+ " dollars."