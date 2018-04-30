
# to allow us to separate our code into different files, programmers divide large programs
# into multiple pieces called MODULES 
	# python also has BUILT IN MODULES --> contain important functionality

# Importing Built-In Modules
	# to use a module, must first IMPORT it
	# syntax: import module_name

import math
math.pow(2,3) 
	
	# MUST CALL THE MODULE EVERYTIME WE CALL A FUNCTION FROM IT

import random
random.randint(0,100) # this function generates a random integer between 0 and 100

import statistics

nums = [1, 2, 3, 4, 5]
statistics.mean(nums) # 3
statistics.median(nums) # 3
statistics.mode(nums) # no unique mode found --> ERROR

# Importing Other Modules
	# the code from the module imported runs when imported
		# so if there is some blatant print expression in the imported module,
		# it will print when we import it

		# to avoid this issue, do a condition 
			# if "__name__ == __main__" then print

			
