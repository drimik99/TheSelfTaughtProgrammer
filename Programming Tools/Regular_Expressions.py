# regular expression: a sequence of characters that define a search pattern
	# -c flag tells Python you are going to pass it a string containing Python code
	# when python executes "import this", it prints the Zen of Python (a poem)
		# it's like an Easter egg

		# export GREP_OPTIONS='--color=always'-> sets grep to print matched words in red in the output
		# then do grep Beautiful zen.txt
			# grep takes in two parameters: 
				# 1) a regular expression (e.g. Beautiful)
				# 2) the filepath of the file to search for the pattern defined in the regular expression (e.g. zen.txt)


	# -i flag -> ignores upper/lower case sensitivity 

	# by default, grep prints the entire line (of the file) it found a match in 
		# -o flag -> prints the exact words only that match the pattern you passed in

	# can use regular expressions with RE MODULE
		# the module comes with a method called FINDALL
			# pass in a regular expression as a parameter and a string
				# findall returns a list with all the items in the string that the pattern matches


# Match Beginning and End
	# can create regular expressions that match complex patterns by adding SPECIAL CHARACTERS
		# use ^ (caret) character to create a regular expression that only matches pattern if
			# pattern occurs at the BEGINNING OF A LINE
		# similarly, adding $ to only match the lines that end with a parameter

grep idea.$ zen.txt # searches for lines that end with idea
grep ^If zen.txt # searches for lines where it starts with If

# Repetition
	# * symbol adds repitition to your regular expressions 