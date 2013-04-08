#emilywang
#softdes!
#tictactoe

def play(board, you, move):
	if move in tictactoe_dict['x'] or tictactoe_dict['o']:	
		print ("Hey, this spot is already occupied!")
		return False
	else:
		tictactoe_dict[you].append(move)
	return board

def visualize_board (board):
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

	#initial values :D
	#board = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
	board = {'x':[], 'o':[]}
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
		move = int(input("Player of " + you + ", make your move. "))

		#python's doing it to the board
		newboard = play (board, you, move)
		while newboard == False:
			move = int(input("Player of " + you + ", try again elsewhere. "))
			newboard = play(board, you, move)
		
		#player made a move; now show them the new board
		print(visualize_board(board))
		
		#next player's turn!
		if you == 'x':
			you = 'o'
		else: 
			you = 'x'

		#setting up the board for the next turn. 	
		board = newboard 

	if you =='x': #because right now you == the loser
		the_end = "Congratulations! Player o is victorious."
	else: 
		the_end = "Congratulations! Player x is victorious."

	print (the_end)

tictactoe()