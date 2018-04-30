
# learning to use a command line interface called Bash
# 	a program we type instructions into that your OS executes
# 	Bash interface comes with most Unix-like operator systems

# command-line is the "control center" for everything

# Commands
	# 	echo -> like print in Python
	# 		e.g. echo hello will print hello

	# 	key: when you see the $ sign followed by a command, it means you need to type that
	# 		into command line


	# 	history -> allows you to see your recent commands

# Relative vs Absolute Paths
	# 	directory = a folder on computer
	# 	pwd -> prints working directory

	# 	the OS represents its directories and locations with a tree (a data structure)
	# 		each branch of the tree is a directory 
	# 		the branches show how the directories connect to each other

	# whenever you are using Bash, you are at a location in your OS's tree 
	# path = location at the tree
	# two ways to give path: absolute and relative

	# absolute path = location of file/directory from root directory
		# e.g. /home/bernie/projects where the first slash represents root directory

	# relative path = starts with current working directory instead of root
		# if path doesn't start with forward slash, then Bash knows you are using relative path

# Navigating 
	# cd -> change directories
	# cd / -> navigate to root directory
	# mkdir (name) -> create new directory with name
		# names cannot have spaces in them
		# e.g. mkdir tstp creates folder titled tstp in wd
	# cd ~ -> go to home directory
	# rmdir (name) -> delete directory name

# Flags
	# a concept in commands that allow the issuer of the command to change command's behavior
	# these are options for commands that can have a value of either True or False
		# by default, all of a command's flags start set to FALSE
			# adding a flag changes flag value to TRUE and behavior of command changes
	# SET FLAG TO TRUE BY PUTTING ONE - HYPHEN SYMBOL BEFORE NAME OF FLAG (which depends on OS)
		# e.g. can do ls -author which prints all of the directories and files in a directory
			# AND ALSO THE NAMES OF THE AUTHORS, people that created them

# Hidden Files
	# the OS and many programs on the computer store data in hidden files
	# files that are not shown to users by default because changing them could affect programs 
		# that depend on them
	# these files start with a period
	# ls -a -> view all files including hidden ones
		# -a -> represents "for all"
	# touch -> creates new file from command line
		# can create hidden files through touch

# pipes
	# the | character is called a pipe
	# can use a pipe to pass the output of a command to another command as its input

# Environmental Variables
	# variables stored in your OS that programs can use to get data about the environment they are 
		# running in 
	# created by EXPORT VARIABLE_NAME = VARIABLE_VALUE
		# to reference an environmental variable in Bash, must use the $ SYMBOL BEFORE ITS NAME

export x = 100
$x

	# environmental variable only exists in the Bash window you created it in
		# can persist this variable by adding it to a hiddle file in your home directory called .profile
			# variable exists as long as it is in your .profile -> delete variable by removing it from there

# Users --> each allowed to use a certain set of operations
	# whoami -> prints name of OS user
	# normally, you are the user you created when you installed your OS
		# BUT THIS IS NOT THE MOST POWERFUL USER IN YOUR OS
		# the highest-level user, who is the user with the highest set of permissions, is called the ROOT USER

	# root user can create and delete other users

	# for security reasons, you do not usually log in as the root user
		# you precede commands that you need to issue as the root user with the command SUDO
		# sudo allows you to issue commands as the root user without compromomising your system's security
			# by logging in as the root user

	# if you have a password, you will be prompted for it whenever you use the sudo command
		# sudo removes safeguards that prevent you from harming the OS
		# don't use sudo unless you know it won't damange your OS



