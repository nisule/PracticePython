userNum = int(input("Please enter a number: "))

divisors = []

for i in range(1, round(userNum/2+1)):
    if (userNum % i == 0):
        divisors.append(i)

print("This is a list of all the divisors of {}! The divisors are:\n{}".format(userNum, divisors))