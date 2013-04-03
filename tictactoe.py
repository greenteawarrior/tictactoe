#emilywang
#softdes!
#tictactoe

#between two human users!

def play(board, you, move):

	"""using the dictionary board = {'x':[4,5], 'o'[1,2]} indicating 
	the current state of the game
	and you either 'x' or 'o' (indicating which player you should move),
	make a perfect computer move.
	The board positions are
	1 2 3
	4 5 6
	7 8 9"""

	if board[move] == 'x' or board[move] == 'o':
		print ("Hey, this spot is already occupied!")
		return False

	else:
		board[move] = you
	return board



def game_over(board):
	#did you win? 
	#also, is there a more concise way to do this?
	
	#horizontal victory
	if board[1] == board[2] == board[3]:
		return True
	if board[4] == board[5] == board[6]: 
		return True
	if board[7] == board[8] == board[9]: 
		return True

	#vertical victory
	if board[1] == board[4] == board[7]: 
		return True
	if board[2] == board[5] == board[8]: 
		return True
	if board[3] == board[6] == board[9]: 
		return True

	#diagonal victory
	if board[1] == board[5] == board[9]: 
		return True
	if board[3] == board[5] == board[7]: 
		return True		

	#nobody has won yet	
	return False 



def tictactoe():
	#board = {} # a dictionary, an empty something.
	#board = [] #let's do a list, actually.
	
	#initial values :D
	board = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9] #shouldn't we start with an unplayed board first?
	you = 'x' #x goes first!

	welcome = """
				Hi there. Let's play tic tac toe! 
				Here's a board; tell me where you want to go. 
				1 2 3
				4 5 6
				7 8 9	
				"""
	print (welcome)

	while game_over(board) == False: 
				#MAKE YO MOVE!
		move = int(input("Player of " + you + ", make your move. "))

		#python's doing it to the board
		newboard = play (board, you, move)
		while newboard == False:
			move = int(input("Player of " + you + ", try again elsewhere. "))
			newboard = play(board, you, move)
		
		#player made a move; now show them the new board
		visualboard = str(board[1]) + " " + str(board[2]) + " " + str(board[3]) + "\n" + str(board[4]) + " " + str(board[5]) + " " + str(board[6]) + "\n" + str(board[7]) + " " + str(board[8]) + " " + str(board[9]) + "\n"    
		print (visualboard)
		
		#next player's turn!
		if you == 'x':
			you = 'o'
		else: 
			you = 'x'

		#setting up the board for the next turn. 	
		board = newboard 

	if you =='x': #because right now you == the loser
		the_end = "Congratulations! Player of o is victorious."
	else: 
		the_end = "Congratulations! Player of x is victorious."

	print (the_end)

tictactoe()

# for player in board:
# 	for more in board[player]:
# 		Boardlist[more]=player

# 		['o', 'o', None, None, 'x', 'x'. . .]
# 		you can index the board

# 		going between the board (human readable), the list, and the dictionary

# 		board = {'x': [4,5], 'o': [1,2]}

# write a game_over function
# there are 8 possible ways to win (look at the dictionary things...)
# eventually you need to incorporate strategy too
