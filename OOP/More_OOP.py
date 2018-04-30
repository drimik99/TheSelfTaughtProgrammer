
# Class Variables vs Instance Variables
	# in Python, classes are objects --> of an instance of class "type"
	# have two types of variables: class variables and instance variables
		# so far we've only dealt with instance variables

	# class variables belong to the object Python creates with a class definition & the objects they create
		# define them inside a class just like reguarl variables
		# ACCESS THEM WITH CLASS OBJECTS
		# useful in that they allow you to share data between all of the instances of a class
			# without relying on global variables
			# CLASS VARIABLES LIKE STATIC MEMBER VARIABLES IN C++


class Rectangle():
	recs = []

	def __init__(self, w, l):
		self.width = w
		self.length = l
		self.recs.append((self.width, self.length))

	def print_size(self):
		print("{} by {}".format(self.width, self.length))


r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs) # [(10, 24), (20, 40), (100, 200)]


# Magic Methods
	# every class in Python inherits from a parent class called OBJECT 
	# Python utilizes the methods from Object in different situations like when you print an object

class Lion:
	def __init__(self, name):
		self.name = name

lion = Lion("Josh")
print(lion) # prints the type of lion and the address 

	# when you print Lion object, Python calls the magic method __repr__ from Object class
		# we can override the inherited __repr__ method to change what to print

class Lion:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return self.name

lion = Lion("Josh")
print(lion) # prints Josh


	# Operands in an expression must have a magic method the operator can use to evaluate
		# the expression
		# e.g. for 2 + 2, each integer object has a magic method called __add__ that is called

	# we can define our own __add__ method in a class and use the objects it creates as operands
		# in an expression with addition operator
			# SIMILAR TO OPERATOR OVERLOADING IN C++


class AlwaysPositive():
	def __init__(self, number):
		self.n = number

	def __add__(self, other):
		return abs(self.n + other.n)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y) # prints 10

	# thus, AlwaysPositive objects can be used as operands in an expression with + operator
		# because we defined the __add__ method
		# calls the __add__ method on the first operand object and passes the second operand
			# object as a parameter

# Is
	# keyword is returns True if two objects are the same object and False otherwise
	# using the keyword in an expression evaluates True when both variables POINT to same object
	# use the is keyword to check if a variable is None


