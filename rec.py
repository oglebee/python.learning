import os 
os.system("clear")
import math
pi = float(math.pi)


############################################
#Load in
############################################
class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def get_perimeter(self):
		return 2 * (self.width + self.height)
	def get_area(self):
		return self.width * self.height

def my_rec():
	askw = int(input("Width of your rectangle? "))
	askh = int(input("Height of your rectangle? "))

	myr = Rectangle(askw, askh)

	what = input("Type what you need to know.\nPerimeter\nArea\nEnter: ")

	if (what == "Perimeter") or (what == "perimeter"):
		print(myr.get_perimeter())
	elif(what == "Area") or (what == "area"):
		print(myr.get_area())
	else:
		print("Sorry no info on that.")

class Triangle:
	def __init__(self, base, height):
		self.base = base
		self.height = height
	def get_area(self):
		return (self.base * self.height)/2
	def get_hyp(self):
		return math.sqrt(((self.base)**2) + ((self.height)**2))

def my_tri(): #First triangle branch
	def left_tri():#non right triangle path
		askb = float(input("What is the base of your triangle? "))
		askh = float(input("What is the height of your triangle? "))

		myt = Triangle(askb, askh)

		what = input("What do you need to know?\nArea\nEnter: ")

		if (what == "area") or (what == "Area"):
			print(myt.get_area())
		else:
			print("Sorry, either you messed up input or I haven't avchieved the desired functionality.")
	
	def right_tri(): #right triangle path
		what_need = input('''\n
What information do you need?\n
1 - Hypotenuse\n
2 - Side Leg given side and hypotenuse\n
3 - Side leg given side and angle\n
4 - Angles given adjacent & opposite sides\n
5 - Angles given side & hypotenuse\n
6 - Area
Enter number: ''')
	
	
		def rt1():
			s1ask = float(input("What is the first side of your right triangle? "))
			s2ask = float(input("What is the second side to your right triangle? "))

			rt = Triangle(s1ask, s2ask)
			print(rt.get_hyp())
			


		if (what_need == "1"):
			rt1()
		else:
			print("Sorry")


	rorl = input("Right triangle? y or n")
	if (rorl == "y") or (rorl == "yes") or (rorl == "Y") or (rorl == "Yes"):
		right_tri()
	elif (rorl == "n") or (rorl == "no") or (rorl == "N") or (rorl == "No"):
		left_tri()



class Circle:
	def __init__(self, radius):
		self.radius = radius
	def get_circ(self):
		return (2 * self.radius) * pi
	def get_area(self):
		return (self.radius * self.radius) * pi

def my_cir():
	askr = float(input("What is the radius?\nEnter: "))

	myc = Circle(askr)

	what = input("What do you need to know?\nCircumference\nArea\nEnter: ")

	if (what == "Circumference") or (what == "circumference") or (what == "perimeter"):
		print(myc.get_circ())
	elif (what == "Area") or (what == "area"):
		print(myc.get_area())
	else:
		print("Sorry I don't know that yet.")
##########################################################
#The interaction
##########################################################
askgeo = input("What shape do you want information on?\nTriangle\nRectangle\nCircle\nEnter: ")


if (askgeo == "Triangle") or (askgeo == "triangle"):
	my_tri()
elif (askgeo == "Rectangle") or (askgeo == "rectangle"):
	my_rec()
elif (askgeo == "Circle") or (askgeo == "circle"):
	my_cir()
else:
	print("Sorry! I don't have what you need yet.")
