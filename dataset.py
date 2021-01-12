gitimport os
os.system('clear')

#this is how you add comments
#import os module
#use system call clear to clear module before

########################################
#Some people like making notes graphical like this
#Glossery 
#variables 15-25
#data types 26-45
#strings 50-70
#numbers 75-95
#lists 95-115
########################################


#variable are like a bucket. usually one item.
#case sensitive. camelback or underscore for convention
#variables can be stored, called and changed
#python reads prigrams line by line from the tope down

first_name = "Mike"
last_name = "Bob"

print(first_name + " " + last_name)

##################################
#Learning to code in 2021
##################################
#Data types

name = 'Mike'
age = 27
colors = ["blue", "red", 'green'] #lists can be changed
tuples = ('Tim', 'John', 'Mike') #you cannot change tuples like lists
dictionary = {
	"John": "Pepperoni",
	"Bob": "Mushrooms",
	"Mary": "Cheese"
}
#dictionaries are made of a key and value pair
#separate with commas and new line

boolean_example = True #or False

print(dictionary["Bob"])

####################################################
#strings
####################################################

name = "Mike"
greetings = "Hello, my name is " + name
#print(greetings.upper())
#print(len(greetings))
#print(greetings[11:20])
print(greetings.split(" ")[4])

#excape character can also be used.
#/ or /n are used a lot
#concantanate using plus symbol with strings
##variable.lower .capitalize .title .swapcase
#we can do logic to it len() func.
#square brackets to call the string like a list.
# range of list items separated by :
#split function will create list from string
#/c/pythonstuff/ps/strings.py

##################################################
#numbers bitch
##################################################

#num = 10.25
#print(float(num))
#print(int(num))
print(4%3)

#float-decimal
#integer - whole number
#important for math
#any math can be simply inputed to python
#can convert to float for division
#** is exponents
#% will divide and return the remainder - modulus modulo
#// floor division gives the least integer divisible
#/c/pythonstuff/ps/numbers.py







####################################################
#Lists
####################################################

#other_names = "Wes"
#nums = [1, 2, 3, 4, 5]

names = ["John", "Bob", "Tina"]
#print(names[0])
#names[0] = "Wes"
#names.append("Wes")
#print(names[3] + 10)
#print(names[3][2] + 10)
print(names[len(names) - 1])

#lists can be changed with index number
#.append function adds to the end
#numbers, strings, variables, other lists, dictionaries
#lists can be huge
#len function works for lists as well as strings nums
#line 13 will display the last item in a list