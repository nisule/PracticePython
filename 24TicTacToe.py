# 0 = empty, 1 =  player 1 occupied that space, 2 = player 2 occupied that space
'''This is the backend 2d array that keeps track of which space on the board is an open space, has been marked by
player 1, or been marked by player 2'''
gameBoard = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]


# draws the game board. Board is empty before players mark any spaces and fills up with Xs and Os as they mark spaces
def drawBoard():
    for i in range(3):
        for j in range(3):
            print(" ---- ", end='')
        print("")
        for h in range(4):
            if h < 3:
                if gameBoard[i][h] == 1: # if player 1 marked that space, put an X
                   print("|  {}  ".format("X"), end='')
                elif gameBoard[i][h] == 2: # if player 2 marked that space, put an O
                   print("|  {}  ".format("O"), end='')
                else:
                   print("|     ", end='') # can inject character in spaces here
        print("|")

    for j in range(3):
        print(" ---- ", end='')
    print()


# checks to see if a player has won the game yet (probably a much better way to do this but eh it works fine (i think))
def ifWon(game):
    # diagonal left to right
    if game[0][0] == 1 and game[1][1] == 1 and game[2][2] == 1 or game[0][0] == 2 and game[1][1] == 2 and game[2][2] == 2:
        return game[0][0] # someone won, so it returns the player at that location to tell you who won
    # diagonal right to left
    if game[0][2] == 1 and game[1][1] == 1 and game[2][0] == 1 or game[0][2] == 2 and game[1][1] == 2 and game[2][0] == 2:
        return game[0][2]
    # first row
    if game[0][0] == 1 and game[0][1] == 1 and game[0][2] == 1 or game[0][0] == 2 and game[0][1] == 2 and game[0][2] == 2:
        return game[0][0]
    # second row
    if game[1][0] == 1 and game[1][1] == 1 and game[1][2] == 1 or game[1][0] == 2 and game[1][1] == 2 and game[1][2] == 2:
        return game[1][0]
    # third row
    if game[2][0] == 1 and game[2][1] == 1 and game[2][2] == 1 or game[2][0] == 2 and game[2][1]== 2 and game[2][2] == 2:
        return game[2][0]
    # first column
    if game[0][0] == 1 and game[1][0] == 1 and game[2][0] == 1 or game[0][0] == 2 and game[1][0] == 2 and game[2][0] == 2:
        return game[0][0]
    # second column
    if game[0][1] == 1 and game[1][1] == 1 and game[2][1] == 1 or game[0][1] == 2 and game[1][1] == 2 and game[2][1] == 2:
        return game[0][1]
    # third column
    if game[0][2] == 1 and game[1][2] == 1 and game[2][2] == 1 or game[0][2] == 2 and game[1][2] == 2 and game[2][2] == 2:
        return game[0][2]


    if any(0 in sublist for sublist in game):
        return 0 # no one has one yet ( if there is still a 0, then there is still an open space)

    return 3 # it is a tie ( no open spaces left so no winner )



# player 1 marks a spot, updates gameBoard
def markSpotPlayer1():
    # gets location to mark for player 1
    location = input("Player 1, enter a location to put your X (enter row,column. counting starts at 0. ex: 2,0) : ").strip()
    while not location[0].isdigit() and not location[2].isdigit(): # checks to see that numbers were input in proper place
        location = input(
            "Player 1, enter a location to put your X (enter row,column. counting starts at 0. ex: 2,0) : ").strip()
    row = int(location[0]) # convert from string to int
    col = int(location[2])

    while validLocation(row, col) == False: # check to see that the location is valid, loops until location is valid
        location = input(
            "Player 1, enter a location to put your X (enter row,column. counting starts at 0. ex: 2,0) : ")
        while not location[0].isdigit() and not location[2].isdigit():
            location = input(
                "Player 1, enter a location to put your X (enter row,column. counting starts at 0. ex: 2,0) : ").strip()
        row = int(location[0])
        col = int(location[2])
    gameBoard[row][col] = 1 # marks spot as occupied by player 1


# player 2 marks a spot, updates gameBoard. Pretty much exactly the same as markSpotPlayer1 but its for player 2.
def markSpotPlayer2():
    location = input(
        "Player 2, enter a location to put your O (enter row,column. counting starts at 0. ex: 2,0) : ").strip()
    while not location[0].isdigit() and not location[2].isdigit():
        location = input(
            "Player 2, enter a location to put your O (enter row,column. counting starts at 0. ex: 2,0) : ").strip()
    row = int(location[0])
    col = int(location[2])

    while validLocation(row, col) == False:
        location = input(
            "Player 2, enter a location to put your O (enter row,column. counting starts at 0. ex: 2,0) : ")
        while not location[0].isdigit() and not location[2].isdigit():
            location = input(
                "Player 2, enter a location to put your O (enter row,column. counting starts at 0. ex: 2,0) : ").strip()
        row = int(location[0])
        col = int(location[2])
    gameBoard[row][col] = 2 # marks spot as occupied by player 2

# checks if the spot the user tried to mark is valid, returns true if it is valid, false otherwise
def validLocation(r, c):
    validNums = "012" # coords go from 0,0 to 2,2 so these are all potential numbers
    if str(r) not in validNums or str(c) not in validNums: # checks that the location entered is actually on the board
        print("Location not valid, enter a valid location")
        return False
    if gameBoard[r][c] != 0: # checks that the location is an open space
        print("That location has already been taken, try a different one")
        return False

    return True


if __name__ == '__main__':
    playAgain = 'y'
    while playAgain[0] == 'y':
        drawBoard()
        while ifWon(gameBoard) == 0: # while no one has one yet
            #player 1 takes their turn, redraws the board
            markSpotPlayer1()
            drawBoard()
            if ifWon(gameBoard) == 0: # checks to see if there is a winner after every time a player marks a space
                # player 2 takes their turn, updates the board
                markSpotPlayer2()
                drawBoard()

        if ifWon(gameBoard) != 3: # if it wasnt 3 it must be 1 or 2 which means one of the players won
            print("Player {} won!".format(ifWon(gameBoard)))
        else:
            print("It was a tie!") # it was 3, so it was a tie

        playAgain = input("Would you like to play again? (y/n) : ") # ask user if they want to play again
        playAgain = playAgain.lower()
        if playAgain[0] == 'y': # continue playing
            gameBoard = [[0, 0, 0], # reset gameBoard
                         [0, 0, 0],
                         [0, 0, 0]]
        else:
            print("Exiting game...")
            exit(0)

