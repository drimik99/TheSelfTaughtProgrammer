# Four Pillars: Encapsulation, Abstraction, Polymorphism, Inheritance

# Encapsulation
	# TWO CONCEPTS:
		# 1) groups variables (state) and methods in a single unit -- the object
		# 2) hiding a class's internal data to prevent the CLIENT, the code outside
			# the class that uses the object from directly accessing it


	# for concept 2: we can directly change an instance variable or call a function that does so
		# both ways of work but break interface
			# that's why there are PRIVATE VARIABLES AND PRIVATE METHODS
			# private variables hide a class's internal data to prevent client from using it
				# alternative: public variables


	# PYTHON DOESN'T HAVE PRIVATE VARIABLES 
		# how Python addresses this: NAMING CONVENTIONS

	# if you have a variable or method that caller should not access, 
		# PRECEDE ITS NAME WITH AN UNDERSCORE!!!!!!!!!!!!!!!!!
		# can essentially call this variable or method but at client's risk

# Abstraction
	# process of "taking away or removing characteristics from something in order to 
	# 			  reduce it to a set of essential characteristics"

	# only have classes with variables and mehtods that are of use to solving the problem
		# e.g. Person class doesn't need blood type as a variable if we never use it in any way

# Polymorphism
	# "the ability to present the same interface for differing underlying forms (data types)"
		# interface = a function or method

# Inheritance
	# child class inherits from parent class
		# DONE BY PASSING PARENT CLASS AS PARAMETER TO CHILD CLASS WHEN YOU CREATE IT

class Shape(): 
	###

class Square(Shape):
	pass 

	# the Square class inherts the Shape class's variables and mehtods
		# only suite you defined in the Square class was the keyword PASS -- tells python to do nothing


	# when child class inherits method from parent class, you can override it by defining 
	# new method with the same name as inherited method
		# METHOD OVERRIDING 

# Composition
	# models the "has a" relationship by storing an object as an instance variable in another object

class Dog():
	def __init__(self, name, breed, owner):
		self.name = name
		self.breed = breed
		self.owner = owner

class Person():
	def __init__(self, name):
		self.name = name


mickey = Person("Mickey Mouse")
bully = Dog("bully", "Bulldog", mickey)

print(bully.owner.name) # prints Mickey Mouse

	# the bully object has an owner - a Person object named "Mickey Mouse" - stored in the 
	# owner instance variable	

