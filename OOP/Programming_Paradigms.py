# programming paradigm is a style of prgoramming 
# we learn about procedural, functional and object oriented programming

# State
	# is the value of a program's variables while it is running
		# this is one of the differences between the various programming paradigms 
	# global state = value of globals while program is running

# Procedural Programming
	# what we did in part 1
	# a programming style in which we write a sequence of steps moving toward a solution 
		# with each step changing program's state
	# like "do this, then do that"
	
	# it is fine for small programs, but not for large one as then we have to always
	# deal with global variables --> hard to keep track

# Functional Programming
	# addresses problem of procedural programming by eliminating global state
	# relies on functions that do not use or change global state
		# only state they use are the parameters you pass to functions

	# basically where you avoid global state by passing variables into functions

	# example:

	a = 0 

	def increment():
		global a
		a += 1

	# OR

	def increment(a):
		return a += 1

	# first version has side effects (changing of global state) but second doesn't

# OOP
	# every object is an INSTANCE of the class
	# in python, a class is a compound statement with HEADER AND SUITE
		# a suite in a class can be a simple statement or compound statement called METHOD
		# methods like functions except in side a class
		# methods defined in the same way as functions except
			# 1) must define method as a suite in a class
			# 2) has to accept at least one parameter (except in special cases)

	# by convention, you always name the first parameter of a method SELF
		# the reason why you need at least one parameter for a method is because
		# when you call a method on an object, Python automatically passes the object 
		# that called the method to the method as a parameter

	# use self to define an INSTANCE VARIABLE, a variable that belongs to an object
		# these are like member variables in C++ (NOT NECESSARILY PRIVATE)
	
	# how to define instance variables: SELF.VARIABLE_NAME = VARIABLE_VALUE
		# normally define instance variables inside a special method called __init__
			# BASICALLY A CONSTRUCTOR --> __init__ runs when object created 

	class Orange:
		def __init__(self, w, c):
			self.weight = w
			self.color = c
			print("Created!")

	# two instance variables of orange: weight and color
	# ANY METHOD SURROUNDED BY DOUBLE UNDERSCORES IS CALLED A MAGIC METHOD
		# a method Python uses for special purposes like creating an object

	# how to define an instance of the class

	or1 = Orange(10, "dark orange") 
	# KEY: don't have to pass in self, Python does that for you

	# can access class instance variables anywhere --> e.g.

	or1.weight = 3
	print(or1.color) # dark orange

	# IMPORTANT: ALL INSTANCE VARIABLES MUST BE DEFINED WITHIN INIT FIRST

	# benefits of OOP: less code duplication and easier to maintain code
	# disadvantage of OOP: lot of planning required





