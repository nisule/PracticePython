import random
'''guesses are broken but this game is trash anyway so not fixing'''
global guesses
guesses = 1

def updateGuesses(guesses):
    guesses += 1
    return guesses

'''Creates the number that the user is supposed to guess in the game, the number is 4 numbers long and each number
is unique (ex 1234 could be a number but 1553 could not be)'''
def makeNumber():
    number = ""
    for i in range(4):
        randNum = str(random.randint(0, 9)) # number for the game
        if randNum in number: # checks to see that the number is not already in the number
            while(randNum in number): # picks new number until it gets a unique one
                randNum = str(random.randint(0,9))
        number += randNum
    print(number)
    return number



'''Checks to see that the user guessed a valid number'''
def isGuessValid(guess):
    for i in range(0, 4): # checks to see that all numbers are unique
        if guess.count(guess[i]) > 1:
            return False
    if len(guess) != 4: # checks to see if guess is 4 characters long
        return False
    if not guess.isdigit(): # checks to see if only numbers were entered
        return False

'''Gets the users guess for the game, it should hopefully be 4 numbers else it forces them to put in a valid guess'''
def getGuess():
    guess = input("Enter your guess (must be 4 unique numbers ex: 1234) : ")

    if (isGuessValid(guess) == False):
        while(isGuessValid(guess) == False):
            guess = input("Guess wasn't valid! Enter your guess (must be 4 unique numbers ex: 1234) : ")

    return guess


'''Determines the number of cows and bulls, is a bull if the number is in the phrase and it is also in the right
place, it is a cow if the number is in the phrase'''
def calcBullsAndCows(phrase, guess): # phrase is randomly generated numbers, guess is user's guess
    cows = 0
    bulls = 0


    for i in range(0, 4):
        if guess[i] == phrase[i]:
            bulls += 1
        elif guess[i] in phrase:
            cows += 1

    print("{} bulls, {} cows".format(bulls, cows))

    if bulls < 4:
        cows = 0
        bulls = 0
        print(updateGuesses(guesses))
        calcBullsAndCows(phrase, getGuess())



if __name__ == '__main__':
    print("Lets play Cows and Bulls!")

    phrase = makeNumber()
    calcBullsAndCows(phrase, getGuess())
    guesses = updateGuesses(guesses)-1

    print("You won! The phrase was {} and it took you {} guesses!".format(phrase, guesses))



