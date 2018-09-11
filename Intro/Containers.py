# CHAPTER 5: CONTAINERS

# Methods
	# these are functions closely associated with a given type of data
		# execute code and can return a result just like a function 
		# call methods on objects and we can pass them parameters
		# basically function that "belongs to" an object

	# "Hello".upper() --> 'HELLO'

# Lists
	# def: a container that stores objects in a specific order
	# lists are represented with brackets 
		# two syntaxes to create a list: 
			# 1) can use the list function e.g. fruit = list()
			# 2) or use brackets fruit = []

	# create a list with items by using the [] syntax and place items in it separated by ,
	fruit = ["apple", "banana", "pear"]

	# lists store items in order and add new item to a list using the append method
	# each object added is to the end of the list
	# KEY: lists can store any data type
		# lists are mutable where that means we can add or remove objects from a container
	fruit[1] = "mango"
		# fruit then becomes ["apple", "mango", "pear"]

	# can do indexing just like C++ 
	# can concantenate lists 
	
	# functions that can work on lists
		# .pop([optional index]) --> removes last element and returns it
		# .append(" ")
		# .insert(i, x) --> adds an element x to index i
		# .remove(x) --> removes first item from the list whose value is x
		# .count(x) --> returns number of times x appears
		# .reverse() --> reverse elements of the list in place
		# .copy() --> returns a shallow copy of 
		# len(list_name)

	colors = ["green", "red", "blue"]
	guess = input("Guess a color: ")

	if guess in colors:
		print("You guessed correctly!")
	else:
		print("Wrong guess!")

# Tuples
	# def: a container that stores objects in a specific order
	# MAIN DIFFERENCE: TUPLES ARE IMMUTABLE UNLIKE LISTS
		# therefore, we cannot change their contents
	# cannot modify any items in it, add new items to it, or remove items from it
	# represent tuples with parenthesis

	# two syntaxes for tuples
		# 1) my_tuple = tuple() 
		# 2) my_tuple = () 
			# if only one item, still must put comma after it

	# use of tuples
		# for dealing with values that'll never change
			# e.g. keys in dictionaries

# Dictionaries
	# another built-in container for storing objects
	# link a KEY to the VALUE (both objects)
		# linking is called mapping
	# are mutable --> can add elements to it
	# key difference: don't store objects in specific order unlike tuples and lists
	# can use key to look up a value in a dictionary BUT NOT VICE VERSA
	
	# two syntaxes: 
		# 1) my_dict = dict()
		# 2) my_dict = {}

	# how to add key-value?
		# seperated key from value by COLON 
		# each key-value pair separated by COMMA
		# unlike tuple, don't need comma after key-value pair if only one pair exists

	my_dict = {1:"Apple", 2:"Banana", 3:"Orange"}

	# shell output might list dictionary items in different order because dictionaries
    # DON'T store keys in order

	# can add key-value pairs as dictionary_name[key] = value
	# can look up value by dictionary_name[key]

	# KEY KEY: dictionary keys are immutable whereas dictionary values are mutable
		# string or tuple can be key but not list or a dictionary

	# use "in" keyword to check if key is in dictionary
		# "in" cannot be used to check if value is contained

	# Deletion of key-value pair
		# do del dictionary_name[key]

# Containers in Containers
	# similar idea to vectors in vectors

	lists = []

	oh = [1, 2]
	yea = [3, 4]
	baby = [5, 6]

	lists = [oh, yea, baby] # or lists.append(oh) etc.

	# ESSENTIAL: if we chance any elements of oh, yea or baby --> it changes those corresponding vectors in the lists object

	# can store tuple inside a list, a list inside a tuple and a dictionary inside a list or a tuple

	bday = {"Tul": "06.03.1999", "Drim": "22.02.1999"}
	my_list = [bday]
	print(my_list)
	my_tuple = (bday)
	print(my_tuple)

	# list, tuple, or dictionary can be a value in a dictionary --> just tuples or strings allowed as keys


	
