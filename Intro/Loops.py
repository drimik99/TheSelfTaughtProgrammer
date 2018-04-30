
# For - Loop --> used to iterate through an iterable
	# SYNTAX: for variable_name in iterable_name : instructions_
	# its normal syntax can be used to print lists, tuples, and keys in dictionary

tv = ["GOT", "Narcos", "The Office"]

i = 0
for show in tv:
	new = tv[i]
	new = new.upper()
	tv[i] = new
	i += 1

print(tv) # ['GOT', 'NARCOS', 'THE OFFICE']

	# possible that we may keep track of current item in a list using an 
		# INDEX VARIABLE -> variable holding integer representing an index in an iterable
		# because accessing each item and its index in an iterable is so common,
		# python has another syntax you can use this

tv = ["GOT", "Narcos", "The Office"]

for i, show in enumerate(tv):
	new = tv[i]
	new = new.upper()
	tv[i] = new
	i += 1

	# instead of iterating through tv, you passed tv to enumerate and iterated through the
	# result, which allowed you to add a new variable i that keeps track of the current index

# Range
	# built in function allowing you to create a sequence of integers and use a for loop
	# to iterate through them
	# RANGE FUNCTION TAKES TWO PARAMETERS
		# a number where the sequence starts and where the seq stops (exclusive upper bound)

for i in range(1,4):
	print(i) # 1\n2\n3


# While loop
	# a loop that executes code until expression evaluates to True

x = 10 
while x > 10:
	print({}.format(x))
	x -= 1

# Break statement
	# terminates loop

for i in range(1, 4):
	if i == 2:
		break 
	print(i)
	# output: 1


# Continue statement
	# to stop current iteration of loop and move on to next one

for i in range(1, 4):
if i == 2:
	continue
print(i)
# output: 1\n3

# Nested Loops

list1 = [5, 6, 7, 8]
list2 = [1, 2, 3, 4]
sum = []

for index1 in list1:
	for index2 in list2:
		sum.append(index1 + index2)

print(sum) #[6, 7, 8, 9, 7, 8, 9, 10, 8, 9, 10, 11, 9, 10, 11, 12]





