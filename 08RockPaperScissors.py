import sys # to exit program at the end
while True: # whole game runs in this loop
    # get player 1's choice, repeats until a proper character is entered
    p1choice = input("Player 1, do you pick rock(r), paper(p), or scissors(s)? (r/p/s) : ").lower()
    while p1choice not in "rps":
        p1choice = input("Player 1 please enter a valid choice this time... (r/p/s): ").lower()
    # same thing for player 2 as player 1
    p2choice = input("Player 2, do you pick rock(r), paper(p), or scissors(s)? (r/p/s) : ").lower()
    while p2choice not in "rps":
        p2choice = input("Player 2 please enter a valid choice this time... (r/p/s): ").lower()

    # determines who won the game or if it was a tie and prints a message representing the outcome
    if p1choice == "r" and p2choice == "r":
        print("It is a tie!")
    elif p1choice == "r" and p2choice == "p":
        print("Player 2 wins!")
    elif p1choice == "r" and p2choice == "s":
        print("Player 1 wins!")
    elif p1choice == "p" and p2choice == "r":
        print("Player 1 wins!")
    elif p1choice == "p" and p2choice == "p":
        print("It is a tie!")
    elif p1choice == "p" and p2choice == "s":
        print("Player 2 wins!")
    elif p1choice == "s" and p2choice == "r":
        print("Player 2 wins!")
    elif p1choice == "s" and p2choice == "p":
        print("Player 1 wins!")
    elif p1choice == "s" and p2choice == "s":
        print("It is a tie!")

    # asks user if they want to play again, exits if they don't otherwise whole game runs again
    playAgain = input("Want to play again? (y/n): ")
    if playAgain not in "yY":
        sys.exit(0)
