import datetime

name = input("Please enter your name: ")
age = input("Please enter your age: ")
howMany = input("Please enter how many times you would like the message to be printed: ")
now = datetime.datetime.now()

currentYear = now.year # gets the current year
yearsToHundred = 100 - int(age) # calculates how many years until the user turns 100 years old
targetYear = currentYear + yearsToHundred # the year they will turn 100

for i in range(0, int(howMany)):
    print("Hey {}, you will turn 100 years old in the year {}!".format(name, targetYear))