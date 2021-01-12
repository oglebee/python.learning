import os 
os.system("clear")

# Fizbuz rules as follows;
# print out all numbers from 1 to 100
# if the number can be /3 print fizz
# if the number can be /5 print out buzz
# if the number can be divided by both 3 and 5 print fizzbuzz
num = 1
fizz_count = 0
buzz_count = 0
fizzbuzz = 0

while (num <= 1000000):
	if (num % 3 == 0) and (num % 5 == 0):
		print(str(num) + ": Fizzbuzz!")
		fizzbuzz += 1
	elif(num % 3 == 0):
		print(str(num) + ": Buzz!")
		buzz_count += 1
	elif(num % 5 == 0):
		print(str(num) + ": Fizz")
		fizz_count += 1
	else:
		print(str(num) + ".")
	num += 1

print("________________________________")
print("Fizz\t\tBuzz\t\tFizzBuzz")
print(str("{:,}".format(fizz_count)) + "\t\t" + str("{:,}".format(buzz_count)) + "\t\t" + str("{:,}".format(fizzbuzz)))
print("14\t\t27\t\t6")

#: in curly brackets make whatever comes afer a seperator