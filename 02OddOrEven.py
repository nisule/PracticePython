numEntered = False
while numEntered == False:
    try:
        num = int(input("Please enter a number: "))
        numEntered = True
    except:
        print("Try entering a number(like you were told to the first time)")

if num % 2 == 0:
    print("{} is an even number!".format(num))
else:
    print("{} is an odd number!".format(num))

if num % 4 == 0:
    print("{} is a multiple of 4!".format(num))


numEntered = False
while numEntered == False:
    try:
        num2 = int(input("Please enter a number: "))
        numEntered = True
    except:
        print("Try entering a number(like you were told to the first time)")

numEntered = False
while numEntered == False:
    try:
        check = int(input("Please enter a number: "))
        numEntered = True
    except:
        print("Try entering a number(like you were told to the first time)")

if num2 % check == 0:
    print("{} divides evenly by {}!".format(num2, check))
else:
    print("{} doesn't divide evenly into {}".format(check, num2))