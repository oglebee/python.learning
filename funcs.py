import os
os.system("clear")

#functions do something
#when called, in () arguments get passed through
"""
def nameit(first_name, last_name):
	print("Hello " + first_name + " " + last_name)

fname = input("Enter first name: ")
lname = input("Enter last name: ")

nameit(fname, lname)
"""
#return will just return the outcome of your funciton
#functions always needed to be defined before you call it (top to bottom)
def mathit(num1, num2):
	return (num1 + num2)

outcome = mathit(9, 1)

print(outcome)





