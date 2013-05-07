import random

#emilywang
#softdes!
#tictactoe

def humanmove(board, you, move):
	if move in board['x'] or move in board['o']:	
		print ("Hey, this spot is already occupied!")
		return False
	elif move not in range(1,9):
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

def game_over(board, player):
	#did you win?
	if player == 'player1x':
		you = 'x'
	elif player == 'player2o':
		you = 'o'

	#horizontal victory
	if 1 in board[you] and 2 in board[you] and 3 in board[you]:
		return True
	if 4 in board[you] and 5 in board[you] and 6 in board[you]:
		return True
	if 7 in board[you] and 8 in board[you] and 9 in board[you]:
		return True
	
	#vertical victory
	if 1 in board[you] and 4 in board[you] and 7 in board[you]:
		return True
	if 2 in board[you] and 5 in board[you] and 8 in board[you]:
		return True
	if 3 in board[you] and 6 in board[you] and 9 in board[you]:
		return True
	
	#diagonal victory
	if 1 in board[you] and 5 in board[you] and 9 in board[you]:
		return True
	if 3 in board[you] and 5 in board[you] and 7 in board[you]:
		return True
	
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
		
		while game_over(board, 'player1x') == False and game_over(board, 'player2o') == False:
			
			move = False
			while move == False:
				try: 
					move = int(input("Player of " + current + ", make your move. "))
				except:
					print ('Try again; please type an integer.')
			
			newboard = humanmove (board, current, move) # will either return the newboard dictionary or False
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
		if current == 'o': #if the computer has exited the loop, then that means x won (and current was reassigned to o)
			print ('Player of x is victorious!')
		elif current == 'x':
			print ('Player of o is victorious!')
		return

	elif player1x == 'human' and player2o == 'monkey':
		welcome = "Hi there. Let's play tic tac toe! \nHere's a board; tell me where you want to go. \n1 2 3 \n4 5 6 \n7 8 9"
		print (welcome)
		
		while game_over(board, 'player1x') == False and game_over(board, 'player2o') == False:

			move = False
			while move == False:
				try: 
					move = input("Player of x, please make your move. ")
				except:
					print ('Try again; please type an integer.')

			newboard = humanmove(board, 'x', move) # will either return the newboard dictionary or False
			while newboard == False:
				move = int(input("Player of x, try again elsewhere. "))
				newboard = humanmove(board, 'x', move)
			#player made a move; now show them the new board
			print(visualize_board(board))

			if game_over(board, 'player1x') == True:
				print ('Player 1, the human (x), is victorious.')
			elif game_over(board, 'player1x') == False:
				newboard = monkeymove(board, 'o')
				print ('The monkey has made its move.')
				print (visualize_board(board))
				board = newboard
		#If it's exited the while loop then the monkey must have won because the game_over check for the human already happened near the end of the most recent iteration.
		print ('Player 2, the monkey (o), is victorious.')
		
		return

	elif player1x == 'monkey'  and player2o == 'human':
		
		return	
	elif player1x == 'human' and player2o == 'computer':
		return
	elif player1x == 'computer' and player2o == 'human':
		return
	elif player1x == 'computer' and player2o == 'monkey':
		return
	elif player1x == 'monkey' and player2o == 'computer':
		return

tictactoe('human', 'monkey')