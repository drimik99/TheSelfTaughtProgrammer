# TRIPLE STRINGS
# if string spans more than one line, you have to put it in triple quotes

""" hello darling
	meow
	my my
""" 

# strings are also iterable 
	# can do NEGATIVE INDEXING --> look up items from right to left iteratively

# strings are immutable --> to change characters in string, must make new string

# Concatenation --> can add many strings together using the addition operator
# String multiplication --> "Saw" * 3 = "SawSawSaw"

# Format method
	# can create a new string using this, which looks for occurrences of {} in the string
	# and replaces them with the parameters you pass in

"William {}".format("Folly") # prints 'William Folly'
"damn {} you lookin {}".format("baby", "fine") # prints 'damn baby you lookin fine'

	# useful when creating a string from user input 
		# --> can pass the read in strings as parameters

# Split method
	# can use to separate one string into two or more strings
	# pass the split method a string as a parameter 
		# --> uses that string to divide original string into multiple

"hello baby".split(" ") 
	# RESULT OF SPLIT IS A LIST WITH ALL THE ITEMS SPLIT
		# EXAMPLE ABOVE RESULT: ['hello', 'baby']

# Join method
	# lets you add new characters between every character in a string

letters = "abc"
result = "+".join(letters)
print(result) # 'a+b+c'

	# can turn a LIST OF STRINGS into a single string by calling the join method
	# on an EMPTY STRING and passing the LIST AS A PARAMETER


words = ["hi", "hello", "hola"]
"".join(words) # 'hihellohola'
" ".join(words) # 'hi hello hola'
" b ".join(words) # 'hi b hello b hola'

# String Space
	# use this to remove leading and trailing whitespace from a string

s = "      the     "
s = s.strip()
s # 'the'


# Replace
	# replaces every occurrence of a string with another string
	# first parameter is the string to replace and second is the string to replace with

hello = "all animals are equal"
hello = hello.replace("a", "e")
print(hello) # ell enimels ere equel

# Find an index
	# get index of the first occurrence of a character in a string with index method

"animals".index("m") # 3 --> raises exception if index method does not find match

# In and Not keyword
	# checks if something is "in" or "not in" string

"cat" in "cat in hat" # True
"bat" in "cat in hat" # False
"bat" not in "cat in hat" # True

# Escaping Strings
	# to put double quotes in strings, must do "..\" .... \".." or ' .. "..."' .. "
	# escaping a string means putting a symbol in front of a character that has 
	# special meaning in Python 

	# newline --> \n

# Slicing
	# way to return a new iterable from a subset of the items in another iterable
	# SYNTAX: iterable[start_index:end_index]

fict = ["babe", "chick", "calc", "pen"]
fict[0:3] # ['babe', 'chick', 'calc']
fict[:3] # ['babe', 'chick', 'calc']
fict[1:] # ['chick, 'calc', 'pen']
fict[:] # ['babe', 'chick, 'calc', 'pen']

