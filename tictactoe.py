import random

#emilywang
#softdes!
#tictactoe

def humanmove(board, you, move):
	if move in board['x'] or move in board['o']:	
		print ("Hey, this spot is already occupied!")
		return False
	else:
		board[you].append(move)
	return board

def monkeymove(board, you):
	numbers = [1,2,3,4,5,6,7,8,9]
	availablemoves = []
	xtaken = board['x']
	otaken = board['o']
	for number in numbers:
		if number not in xtaken and number not in otaken:
			availablemoves.append(number)
	move=random.choice(availablemoves)
	board[you].append(move)
	return board

def visualize_board (board):
	"""This function creates a printable version of the board so a human can see the current board."""
	boardposlist = [None,'1','2','3','4','5','6','7','8','9'] 
	xpos = board['x']
	for i in xpos:
	 	boardposlist[i] = 'x'
	opos = board['o']
	for i in opos:
	 	boardposlist[i] = 'o'
	boardstring = str(boardposlist[1]) + " " + str(boardposlist[2]) + " " + str(boardposlist[3]) + "\n" + str(boardposlist[4]) + " " + str(boardposlist[5]) + " " + str(boardposlist[6]) + "\n" + str(boardposlist[7]) + " " + str(boardposlist[8]) + " " + str(boardposlist[9]) + "\n"
	return boardstring

def game_over(board):
	#did you win? 
	#also, is there a more concise way to do this?
	
	for you in board: #you is either the X player or O player
		
		#horizontal victory
		if 1 in board[you] and 2 in board[you] and 3 in board[you]:
			return str(you) + " is victorious."
		if 4 in board[you] and 5 in board[you] and 6 in board[you]:
			return str(you) + " is victorious."
		if 7 in board[you] and 8 in board[you] and 9 in board[you]:
			return str(you) + " is victorious."
		
		#vertical victory
		if 1 in board[you] and 4 in board[you] and 7 in board[you]:
			return str(you) + " is victorious."
		if 2 in board[you] and 5 in board[you] and 8 in board[you]:
			return str(you) + " is victorious."
		if 3 in board[you] and 6 in board[you] and 9 in board[you]:
			return str(you) + " is victorious."
		
		#diagonal victory
		if 1 in board[you] and 5 in board[you] and 9 in board[you]:
			return str(you) + " is victorious."
		if 3 in board[you] and 5 in board[you] and 7 in board[you]:
			return str(you) + " is victorious."
	
	if len(board['x']) + len(board['o']) == 9:
		return "It's a tie."
	else: #nobody has won yet
		return False

def tictactoe(player1x,player2o):
	# initial values
	board = {'x':[], 'o':[]}
	if player1x == 'human' and player2o == 'human':
		current = 'x' #x goes first!
		welcome = "Hi there. Let's play tic tac toe! \nHere's a board; tell me where you want to go. \n1 2 3 \n4 5 6 \n7 8 9"
		print (welcome)
		while game_over(board) == False: 
			move = int(input("Player of " + current + ", make your move. "))
			#python's doing it to the board
			newboard = humanmove (board, current, move)
			while newboard == False:
				move = int(input("Player of " + current + ", try again elsewhere. "))
				newboard = humanmove(board, current, move)
			#player made a move; now show them the new board
			print(visualize_board(board))
			#next player's turn!
			if current == 'x':
				current = 'o'
			else: 
				current = 'x'
			#setting up the board for the next turn. 	
			board = newboard 
		print (game_over(board))
		return
	elif player1x == 'human' and player2o == 'computer':
		return
	elif player1x == 'computer' and player2o == 'human':
		return
	elif player1x == 'human' and player2o == 'monkey':
		return
	elif player1x == 'monkey'  and player2o == 'human':
		return
	elif player1x == 'computer' and player2o == 'monkey':
		return
	elif player1x == 'monkey' and player2o == 'computer':
		return

tictactoe('human', 'human')