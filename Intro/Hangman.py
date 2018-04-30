
def hangman(word):
	wrong = 0
	stages = ["",
			 "						",
			 "_________				",
			 "|						",
			 "|			|			",
			 "|			0			",
			 "|		   /|\			",
			 "|		   / \			",
			 "|						"
			 ]
	 rletters = list(word)
	 board = ["___"] * len(word)
	 word = False
	 print("Welcome to Hangman!")

	 while wrong < len(stages) - 1:
	 	print("\n")
	 	char = input("Guess a letter")
	 	if char in rletters:
	 		board[rletters.index(char)] = char
	 		rletters[rletters.index(char)] = char
	 	else:
	 		wrong += 1
 		print((" ".join(board)))
 		e = wrong + a