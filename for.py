import os
os.system("clear")

############################
# For Loopos
# for loops allow looping through something
# dictionaries, lists, letters in variable
# x is a created variable
#dictionary needs .items function and key,value distinction

#names = ["John", "Bob", "Mary"]
fav_pizza = {
	"John": "Pepperoni",
	"Tim": "Mushroom",
	"Mary": "Cheese",
}

for key,value in fav_pizza.items():
	print(key + " likes " + value + " pizza.")