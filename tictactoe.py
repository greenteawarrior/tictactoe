import random

#emilywang
#softdes!
#tictactoe

def humanmove(board, you, move):
    """This is the human implementation of a tictactoe player."""
    if move in board['x'] or move in board['o']:    
        print ("Hey, this spot is already occupied!")
        return False
    elif move not in range(1,10):
        return False
    else:
        board[you].append(move)
    return board

def monkeymove(board, you):
    """This is a monkey (random) implementation of a tictactoe player."""
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

def play(board, you):
    """This is a computer implementation of a tictactoe player."""
    corners = [1, 3, 7, 9]
    edges = [2, 4, 6, 8]
    center = 5
    move = None

    if you == 'x':
        opponent = 'o'
    if you == 'o':
        opponent = 'x'
    
    numbers = [1,2,3,4,5,6,7,8,9]
    availablemoves = []
    xtaken = board['x']
    otaken = board['o']
    for number in numbers:
        if number not in xtaken and number not in otaken:
            availablemoves.append(number)

    ###
    # The Opening (x) : If computer is x, then take the center spot. (Technically x can win from any starting position, but for this implementation let's always start in the center.)
    if len(availablemoves) == 9:
        move = 5

    if move != None:
        board[you].append(move)
        return board

    # The Opening (o) : If computer is o, then the computer must respond appropriately based on the opponent's first move.
    # Player O must always respond to a corner opening with a center mark, and to a center opening with a corner mark. An edge opening must be answered either with a center mark, a corner mark next to the x, or an edge mark opposite the X.
    if len(board[opponent]) == 1:
        if board[opponent] in corners:
            move  = center
        if board[opponent] == center:
            move = 1 # let's pick the first corner
        if board[opponent] in edges:
            move = center

    if move != None:
        board[you].append(move)
        return board

    ###
    # 1. Win : If the player has two in a row, they can place a third to get three in a row.

    # Horizontal win check
    h_winlist = [1, 4, 7]
    for e in h_winlist:
        if e in board[you] and e+1 in board[you] and e+2 in availablemoves:
            move = e+2
        if e in board[you] and e+2 in board[you] and e+1 in availablemoves:
            move = e+1
        if e+1 in board[you] and e+2 in board[you] and e in availablemoves:
            move = e

    if move != None:
        board[you].append(move)
        return board


    # Vertical win check
    v_winlist = [1, 2, 3]
    for e in v_winlist:
        if e in board[you] and e+3 in board[you] and e+6 in availablemoves: 
            move = e+6
        if e in board[you] and e+6 in board[you] and e+3 in availablemoves:
            move = e+3
        if e+3 in board[you] and e+6 in board[you] and e in availablemoves:
            move = e

    if move != None:
        board[you].append(move)
        return board



    # Diagonal win check 
    # (I don't have an elegant e iteration method for this one.)
    if 1 in board[you] and 5 in board[you] and 9 in availablemoves: 
        move = 9
    if 1 in board[you] and 9 in board[you] and 5 in availablemoves:
        move = 5
    if 5 in board[you] and 9 in board[you] and 1 in availablemoves:
        move = 1
    if 3 in board[you] and 5 in board[you] and 7 in availablemoves: 
        move = 7
    if 3 in board[you] and 7 in board[you] and 5 in availablemoves:
        move = 5
    if 5 in board[you] and 7 in board[you] and 3 in availablemoves:
        move = 3

    if move != None:
        board[you].append(move)
        return board

    print (board)

    ###
    # 2. Block : If the opponent has two in a row, the player must play the third themself to block the opponent.
    # Horizontal block check
    h_blocklist = [1, 4, 7]
    for e in h_blocklist:
        if e in board[opponent] and e+1 in board[opponent] and e+2 in availablemoves:
            move = e+2
        if e in board[opponent] and e+2 in board[opponent] and e+1 in availablemoves:
            move = e+1
        if e+1 in board[opponent] and e+2 in board[opponent] and e in availablemoves:
            move = e

    if move != None:
        board[you].append(move)
        return board

    # Vertical block check
    v_blocklist = [1, 2, 3]
    for e in v_blocklist:
        if e in board[opponent] and e+3 in board[opponent] and e+6 in availablemoves: 
            move = e+6
        if e in board[opponent] and e+6 in board[opponent] and e+3 in availablemoves:
            move = e+3
        if e+3 in board[opponent] and e+6 in board[opponent] and e in availablemoves:
            move = e

    if move != None:
        board[you].append(move)
        return board

    # Diagonal block check 
    # (I don't have an elegant e iteration method for this one.)
    if 1 in board[opponent] and 5 in board[opponent] and 9 in availablemoves: 
        move = 9
    if 1 in board[opponent] and 9 in board[opponent] and 5 in availablemoves:
        move = 5
    if 5 in board[opponent] and 9 in board[opponent] and 1 in availablemoves:
        move = 1
    if 3 in board[opponent] and 5 in board[opponent] and 7 in availablemoves: 
        move = 7
    if 3 in board[opponent] and 7 in board[opponent] and 5 in availablemoves:
        move = 5
    if 5 in board[opponent] and 7 in board[opponent] and 3 in availablemoves:
        move = 3


    if move != None:
        board[you].append(move)
        return board

    ###
    # 3. Fork : Creation of an opportunity where the player has two threats to win (two non-blocked lines of 2).
    # The 12369 fork path (top and right sides)
    if 1 in board[you] and 6 in board[you] and 2 in availablemoves and 3 in availablemoves and 9 in availablemoves:
        move = 3
    if 1 in board[you] and 9 in board[you] and 2 in availablemoves and 3 in availablemoves and 6 in availablemoves:
        move = 3
    if 2 in board[you] and 6 in board[you] and 1 in availablemoves and 3 in availablemoves and 9 in availablemoves:
        move = 3
    if 2 in board[you] and 9 in board[you] and 1 in availablemoves and 3 in availablemoves and 6 in availablemoves:
        move = 3

    if move != None:
        board[you].append(move)
        return board

    # # The 14789 fork path (bottom and left sides)
    if 1 in board[you] and 8 in board[you] and 4 in availablemoves and 9 in availablemoves and 7 in availablemoves:
        move = 7
    if 1 in board[you] and 9 in board[you] and 4 in availablemoves and 8 in availablemoves and 7 in availablemoves:
        move = 7
    if 4 in board[you] and 8 in board[you] and 1 in availablemoves and 9 in availablemoves and 7 in availablemoves:
        move = 7
    if 4 in board[you] and 9 in board[you] and 1 in availablemoves and 8 in availablemoves and 7 in availablemoves:
        move = 7

    if move != None:
        board[you].append(move)
        return board

    # # The 24568 fork path (through the center)
    if 2 in board[you] and 4 in board[you] and 5 in availablemoves and 6 in availablemoves and 8 in availablemoves:
        move = 5
    if 2 in board[you] and 6 in board[you] and 5 in availablemoves and 4 in availablemoves and 8 in availablemoves:
        move = 5
    if 6 in board[you] and 8 in board[you] and 5 in availablemoves and 2 in availablemoves and 4 in availablemoves:
        move = 5
    if 4 in board[you] and 8 in board[you] and 5 in availablemoves and 2 in availablemoves and 6 in availablemoves:
        move = 5
 
    if move != None:
        board[you].append(move)
        return board
    ###
    # 4. Blocking an opponent's fork: If there is a configuration where the opponent can fork, the player should block that fork.
    # Blocking the 12369 fork path (top and right sides)
    if 1 in board[opponent] and 6 in board[opponent] and 2 in availablemoves and 3 in availablemoves and 9 in availablemoves:
        move = 3
    if 1 in board[opponent] and 9 in board[opponent] and 2 in availablemoves and 3 in availablemoves and 6 in availablemoves:
        move = 3
    if 2 in board[opponent] and 6 in board[opponent] and 1 in availablemoves and 3 in availablemoves and 9 in availablemoves:
        move = 3
    if 2 in board[opponent] and 9 in board[opponent] and 1 in availablemoves and 3 in availablemoves and 6 in availablemoves:
        move = 3

    if move != None:
        board[you].append(move)
        return board

    # # Blocking the 14789 fork path (bottom and left sides)
    if 1 in board[opponent] and 8 in board[opponent] and 4 in availablemoves and 9 in availablemoves and 7 in availablemoves:
        move = 7
    if 1 in board[opponent] and 9 in board[opponent] and 4 in availablemoves and 8 in availablemoves and 7 in availablemoves:
        move = 7
    if 4 in board[opponent] and 8 in board[opponent] and 1 in availablemoves and 9 in availablemoves and 7 in availablemoves:
        move = 7
    if 4 in board[opponent] and 9 in board[opponent] and 1 in availablemoves and 8 in availablemoves and 7 in availablemoves:
        move = 7

    if move != None:
        board[you].append(move)
        return board

    # # The 24568 fork path (through the center)
    if 2 in board[opponent] and 4 in board[opponent] and 5 in availablemoves and 6 in availablemoves and 8 in availablemoves:
        move = 5
    if 2 in board[opponent] and 6 in board[opponent] and 5 in availablemoves and 4 in availablemoves and 8 in availablemoves:
        move = 5
    if 6 in board[opponent] and 8 in board[opponent] and 5 in availablemoves and 2 in availablemoves and 4 in availablemoves:
        move = 5
    if 4 in board[opponent] and 8 in board[opponent] and 5 in availablemoves and 2 in availablemoves and 6 in availablemoves:
        move = 5
 
    if move != None:
        board[you].append(move)
        return board

    # 5. Center : If the computer has the first move of the game, play in the center.
    if 5 in availablemoves:
        move = 5
    
    if move != None:
        board[you].append(move)
        return board

    # 6. Opposite corner : If the opponent is in the corner, the player plays the opposite corner.
    if 1 in board[opponent] and 9 in availablemoves:
        move = 9
    if 3 in board[opponent] and 7 in availablemoves:
        move = 7 
    if 9 in board[opponent] and 1 in availablemoves:
        move = 1
    if 7 in board[opponent] and 3 in availablemoves:
        move = 3

    if move != None:
        board[you].append(move)
        return board

    # 7. Empty corner: The player plays in the corner square.
    if 1 in availablemoves:
        move = 1
    if 3 in availablemoves:
        move = 3
    if 7 in availablemoves:
        move = 7
    if 9 in availablemoves:
        move = 9

    if move != None:
        board[you].append(move)
        return board

    # 8. Empty side: The player plays in a middle square on any of the 4 sides.
    if 1 in availablemoves and 2 in availablemoves and 3 in availablemoves:
        move = 2
    if 4 in availablemoves and 5 in availablemoves and 6 in availablemoves:
        move = 5
    if 7 in availablemoves and 8 in availablemoves and 9 in availablemoves:
        move = 8
    if 1 in availablemoves and 4 in availablemoves and 7 in availablemoves:
        move = 4
    if 2 in availablemoves and 5 in availablemoves and 8 in availablemoves:
        move = 5
    if 3 in availablemoves and 6 in availablemoves and 9 in availablemoves:
        move = 6

    if move != None:
        board[you].append(move)
        return board

    return board


def visualize_board (board):
    """This function creates a printable version of the board so a human can see the current board."""
    boardposlist = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
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
        return 'Draw'
    else: #nobody has won yet
        return False

    print ('SUPARGH')
    return False

def tictactoe():

    welcome = "Hi there. Let's play tic tac toe! \nHere's a board; tell me where you want to go. \n1 2 3 \n4 5 6 \n7 8 9\n\nIf you would like to play tictactoe with another computer implementation, please import the 'play' function from Emily's tictactoe module and proceed from there."
    print (welcome)

    possibleplayerlist = ['human', 'monkey', "computer"]
    player1x = None
    player2o = None
    
    #determine player1 and player2

    while player1x not in possibleplayerlist:
        try:
            player1x = str(input("Player 1 is a... (type and enter one of the available options: \nhuman\nmonkey\ncomputer\n"))
        except:
            print ("Invalid player 1 option. Please type again.")

    while player2o not in possibleplayerlist:
        try:
            player2o = str(input("Player 2 is a... (type and enter one of the available options: \nhuman\nmonkey\ncomputer\n"))
        except:
            print ("Invalid player 2 option. Please type again.")

    # initial values
    board = {'x':[], 'o':[]}
    
    if player1x == 'human' and player2o == 'human':
        print ('Player 1 (x) goes first.')
        current = 'x' #x goes first!

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
        if game_over(board,'player1x') != 'Draw' and current == 'o': #if the computer has exited the loop, then that means x won (and current was reassigned to o)
            print ('Player of x is victorious!')
        elif game_over(board, 'player1x') == 'Draw':
            print ("It's a tie.")
        else: #current == 'x'
            print ('Player of o is victorious!')
        return

    elif player1x == 'human' and player2o == 'monkey':
        print("\nThe human will go first and is player x; monkey is player o.\n")
        
        while game_over(board, 'player1x') == False and game_over(board, 'player2o') == False:

            move = False
            while move == False:
                try: 
                    move = int(input("Player of x, please make your move. "))
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
                return
            elif game_over(board, 'player1x') == 'Draw':
                print ("It's a tie.")
                return
            elif game_over(board, 'player1x') == False:
                newboard = monkeymove(board, 'o')
                print ('The monkey has made its move.')
                print (visualize_board(board))
                board = newboard
        #If it's exited the while loop then the monkey must have won because the game_over check for the human already happened near the end of the most recent iteration.
        print ('Player 2, the monkey (o), is victorious.')
        return

    elif player1x == 'monkey'  and player2o == 'human':
        print('\nThe monkey will go first and is player x ; human is player o.\n')
        
        while game_over(board, 'player1x') == False and game_over(board, 'player2o') == False:
            
            newboard = monkeymove(board, 'x')
            print ('The monkey has made its move.')
            print (visualize_board(board))
            board = newboard

            if game_over(board, 'player1x') == True:
                print ('Player 1, the monkey, is victorious.')
                return
            elif game_over(board, 'player1x') == 'Draw':
                print ("It's a tie.")
                return
            elif game_over(board, 'player1x') == False:
                move = False
                while move == False:
                    try: 
                        move = int(input("Player of o, please make your move. "))
                    except:
                        print ('Try again; please type an integer.')

                newboard = humanmove(board, 'o', move) # will either return the newboard dictionary or False
                while newboard == False:
                    move = int(input("Player of o, try again elsewhere. "))
                    newboard = humanmove(board, 'o', move)
                #player made a move; now show them the new board
                print(visualize_board(board))
                
        #If it's exited the while loop then the human must have won because the game_over check for the monkey already happened near the end of the most recent iteration.
        print ('Player 2, the human (o), is victorious.')
        return  

    elif player1x == 'human' and player2o == 'computer':
        print("\nThe human will go first and is player x; computer is player o.\n")
        
        while game_over(board, 'player1x') == False and game_over(board, 'player2o') == False:

            move = False
            while move == False:
                try: 
                    move = int(input("Player of x, please make your move. "))
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
                return
            elif game_over(board, 'player1x') == 'Draw':
                print ("It's a tie.")
                return
            elif game_over(board, 'player1x') == False:
                newboard = play(board, 'o')
                print ('The computer has made its move.')
                print (visualize_board(board))
                board = newboard
        #If it's exited the while loop then the computer must have won because the game_over check for the human already happened near the end of the most recent iteration.
        print ('Player 2, computer (o), is victorious.')
        return

    elif player1x == 'computer' and player2o == 'human':
        print('\nThe computer will go first and is player x ; human is player o.\n')
        
        while game_over(board, 'player1x') == False and game_over(board, 'player2o') == False:
            newboard = play(board, 'x')
            print ('The computer has made its move.')
            print (visualize_board(board))
            board = newboard
            if game_over(board, 'player1x') == True:
                print ('Player 1, the computer, is victorious.')
                return
            elif game_over(board, 'player1x') == False:
                move = False
                while move == False:
                    try: 
                        move = int(input("Player of o, please make your move. "))
                    except:
                        print ('Try again; please type an integer.')

                newboard = humanmove(board, 'o', move) # will either return the newboard dictionary or False
                while newboard == False:
                   print ('supNew')
                   move = int(input("Player of o, try again elsewhere. "))
                   newboard = humanmove(board, 'o', move)
                #player made a move; now show them the new board
                print(visualize_board(board))
            elif game_over(board, 'player1x') == 'Draw':
                print ("It's a tie.")
                return
                
        #If it's exited the while loop then the human must have won because the game_over check for the monkey already happened near the end of the most recent iteration.
        print ('Player 2, the human (o), is victorious.')
        return

    elif player1x == 'computer' and player2o == 'monkey':
        print ("\nThe computer will go first and is player x ; monkey is player o.\n")
        totalgames = int(input("How many games would you like the computer and monkey to play?\n"))
        
        #initialize counters
        draws = 0
        mwins = 0
        cwins = 0

        for i in range(0, totalgames):
            board = {'x':[], 'o':[]}
            while game_over(board, 'player1x') == False and game_over(board, 'player2o') == False:
                board = play(board, 'x')
                print ('The computer has made its move.')
                print (visualize_board(board))

                if game_over(board, 'player1x') == True:
                    print ('Player 1, the computer (x), is victorious.')
                    cwins += 1
                elif game_over(board, 'player1x') == 'Draw' and game_over(board, 'player2o') == 'Draw':
                    print ("It's a tie.")
                    draws += 1
                elif game_over(board, 'player1x') == False and game_over(board, 'player2o') == False:
                    board = monkeymove(board, 'o')
                    print ('The monkey has made its move.')
                    print (visualize_board(board))
                    if game_over(board, 'player2o') == True:
                        print ('Player 2, the monkey (o), is victorious.')
                        mwins += 1
                    elif game_over(board, 'player2o') == 'Draw':
                        print ("It's a tie.")
                        draws += 1

        print ("X (computer) won "+ str(cwins) + " times; O (monkey) won " + str(mwins) + " times; "+ str(draws) +" ties." )
        return

    elif player1x == 'monkey' and player2o == 'computer':
        print ("\nThe monkey will go first and is player x ; computer is player o.\n")
        totalgames = int(input("How many games would you like the computer and monkey to play?\n"))
        
        #initialize counters
        draws = 0
        mwins = 0
        cwins = 0

        for i in range(0, totalgames):
            #print ('current i', i)
            board = {'x':[], 'o':[]}
            #print ('draws', draws)
            #print ('mwins', mwins)
            #print ('cwins', cwins)
            while game_over(board, 'player1x') == False and game_over(board, 'player2o') == False:
                print (board)
                board = monkeymove(board, 'x')
                print ('The monkey has made its move.')
                print (board)
                print (visualize_board(board))

                if game_over(board, 'player1x') == True:
                    print ('Player 1, the monkey (x), is victorious.')
                    mwins += 1
                elif game_over(board, 'player1x') == 'Draw' and game_over(board, 'player2o') == 'Draw':
                    print ("It's a tie.")
                    draws += 1
                elif game_over(board, 'player1x') == False and game_over(board, 'player2o') == False:
                    board = play(board, 'o')
                    print ('The computer has made its move.')
                    print (visualize_board(board))
                    if game_over(board, 'player2o') == True:
                        print ('Player 2, the computer (o), is victorious.')
                        cwins += 1
                    elif game_over(board, 'player2o') == 'Draw':
                        print ("It's a tie.")
                        draws += 1

        print ("X (computer) won "+ str(cwins) + " times; O (monkey) won " + str(mwins) + " times; "+ str(draws) +" ties." )
        return

if __name__=="__main__":
    tictactoe()
