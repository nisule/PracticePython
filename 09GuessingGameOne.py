import random
import sys

randNum = random.randint(1, 10) # random number between 1 and 9

num = input("A number between 1 and 9 (inclusive) has been randomly generated. Guess the number: ")
guesses = 1
if num == "exit":
    sys.exit(0)

num = int(num) # casts to int

while num != randNum: # while the user hasnt guessed the number
    if num < randNum: # guess is too low
        num = input("{} is too low! Guess again! : ".format(num)) # have them guess again
        if num == "exit":
            sys.exit(0)

        num = int(num)
        guesses += 1 # increment number of guesses
    elif num > randNum: # same as above if statement but if guess is too high
        num = input("{} is too high! Guess again! : ".format(num))
        if num == "exit":
            sys.exit(0)

        num = int(num)
        guesses += 1

print("You guessed it! The number was {}! It took you {} guesses to get it right!".format(randNum, guesses))
if guesses > 3:
    print("Wow! That took a lot of guesses for you to get it! Unlucky!")
if guesses == 2 or guesses == 3:
    print("Not bad! Only {} guesses!".format(guesses))
if guesses == 1:
    print("What a lucky guess!!")