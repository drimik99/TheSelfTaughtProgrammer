
# first step to working with a file is to open it with Python's built in open function
	# open func takes 2 parameters: 
		# string representing path to file to open 
		# string representing the mode to open the file in


	# the path to the file or FILE PATH represents location on computer where file exists
	# use OS MODULE to avoid problems with your program working across different operating systems

import os
os.path.join("Users", "Bob", "s.txt") # 'Users/Bob/s.txt'	

	# the mode you pass to the open function determines the actions you will be able
	# to perform on the file you open
		# "r" --> opens file for reading only
		# "w" --> opens file for writing only
		# "w+" --> opens file for reading and writing 

	# the open function returns a FILE OBJECT, which you can use to read and/or write
		# when you use "w" as your mode, the open function creates a new file if it 
		# doesn't already exist in the directory that your program is running in

	# must CLOSE the file object when done like .close()

# Automatically Closing Files
	# can do this syntax where python closes file when program finishes running

with open("st.txt", "w") as f:
	f.write("hello from python!")

	# IMPORTANT: "as" keyword allows you to create aliases

# Reading from Files
	# passing "r" as your mode --> you can then call READ() func, which returns
	# an iterable containing each line of the file


with open("st.txt", "r") as f:
	print(f.read())

	# can only read file once --> should save contents if you need it when you read it

mylist = []

with open("st.txt", "r") as f:
	mylist.append(f.read())


# CSV files
	# a DELIMITER is a symbol, like a comma or a vertical bar |, used to separate
	# data in a CSV file 

	# a file with one,two,three four,five,six when opened in excel would be
		# one two and three would each get a cell in the first row
		# three four and five would each get a cell in the second row

	# CSV module has a METHOD called WRITER that accepts a file object and delimiter
		# writer returns a csv object that has a method called WRITEROW
			# this method accepts a list as a parameter and you can use it to
			# write to a csv file
				# every item in the list gets separated by the delimiter you passed
				# in the writer method to A ROW IN THE CSV FILE 
					# therefore, writerow creates only one row

import csv

with open("st.csv", "w", newline = '') as f:
	w = csv.writer(f, delimiter = ",")

	w.writerow(["one", "two", "three"])
	w.writerow(["four", "five", "six"])

	# this creates a st.csv file with contents that look like
	# one,two,three
	# four,five,six


	# can also use the csv module to read contents of a file 
		# pass "r" as mode and use READER method instead of WRITER with , as delimiter
		# returns an iterable you can use toa ccess each row in the file

with open("st.csv", "r") as f:
	w = csv.reader(f, delimiter = ",")
	for row in w:
		print(",".join(row))

