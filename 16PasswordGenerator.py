import random
import sys


'''gets input from user on if they want a random or word password
returns true for random password, false for word'''
def RandomOrWord():
    response = input("Do you want a random or word password? (r/w): ")
    response = response.lower()

    if response[0] == "r":
        return True
    elif response[0] == "w":
        return False
    else:
        sys.exit(0)


# generates a password, created from random characters
def GenRandom():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+[]\{}|,./<>?"
    password = ""
    r = random.SystemRandom()
    length = int(input("How long do you want your password to be? (ex: 12) : "))

    for i in range(0, length):
        password += chars[r.randint(0, len(chars)-1)]
    return password


# generates a password, picks 2 random words from dictionary
def GenWord():
    length = int(input("How many words do you want your password to be? (ex: 4) : "))

    with open("dictionary.txt") as f: # opens file
        content = f.readlines() # reads file
        content = [x.strip() for x in content] # makes contents prettier
        dictionary = [] # the list of words we will use
        for word in content:
            if len(word) >= 3 and len(word) <= 8: # words of appropriate length add to dictionary
                dictionary.append(word)
        password = ""
        r = random.SystemRandom()
        for i in range(0, length):
            password += dictionary[r.randint(0, len(dictionary)-1)] + " " # picks a random word for password

        f.close() # close file
    return password


if __name__ == '__main__':
    while(True): # keeps asking if you want a password
        if RandomOrWord() == True:
            print(GenRandom())
        else:
           print(GenWord())