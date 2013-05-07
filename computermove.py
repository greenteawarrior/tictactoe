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

def play(board, you):
    """This is a computer implementation of a tictactoe player."""
    corners = [1, 3, 7, 9]
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
    # 1. Win : If the player has two in a row, they can place a third to get three in a row.

    # Horizontal win check
    h_winlist = [1, 4, 7]
    for e in h_winlist:
        if e in board[you] and e+1 in board[you] and e in availablemoves:
            move = e+2
        if e in board[you] and e+2 in board[you] and e in availablemoves:
            move = e+1
        if e+2 in board[you] and e+3 in board[you] and e in availablemoves:
            move = e

    if move != None:
        board[you].append(move)
        return board

    # Vertical win check
    v_winlist = [1, 2, 3]
    for e in v_winlist:
        if e in board[you] and e+3 in board[you] and e in availablemoves: 
            move = e+6
        if e in board[you] and e+6 in board[you] and e in availablemoves:
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


    ###
    # 2. Block : If the opponent has two in a row, the player must play the third themself to block the opponent.
    # Horizontal block check
    h_blocklist = [1, 4, 7]
    for e in h_blocklist:
        if e in board[opponent] and e+1 in board[opponent] and e in availablemoves:
            move = e+2
        if e in board[opponent] and e+2 in board[opponent] and e in availablemoves:
            move = e+1
        if e+2 in board[opponent] and e+3 in board[opponent] and e in availablemoves:
            move = e

    if move != None:
        board[opponent].append(move)
        return board

    # Vertical block check
    v_blocklist = [1, 2, 3]
    for e in v_blocklist:
        if e in board[opponent] and e+3 in board[opponent] and e in availablemoves: 
            move = e+6
        if e in board[opponent] and e+6 in board[opponent] and e in availablemoves:
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


# #Horizontal win check
# board={'x':[4,5],'o':[1,2]}
# print (visualize_board(board))
# print 
# play(board,'x')
# print (visualize_board(board))

# #Vertical win check
# board={'x':[1,4],'o':[]}
# print (visualize_board(board))
# print 
# play(board,'x')
# print (visualize_board(board))

#Diagonal win check
# board={'x':[3,5],'o':[1,2]}
# print (visualize_board(board))
# print 
# play(board,'x')
# print (visualize_board(board))

# #Horizontal block check
# board={'x':[],'o':[4,6]}
# print (visualize_board(board))
# print 
# play(board,'x')
# print (visualize_board(board))

# #Vertical block check
# board={'x':[],'o':[1,7]}
# print (visualize_board(board))
# print 
# play(board,'x')
# print (visualize_board(board))