def main():
    checkPrime(getInt())



def getInt():
    return int(input("Enter a number to see if it is prime or not : "))

def checkPrime(num):
    if num == 0:
        print("{} is not a prime number!".format(num))
        return False
    if num == 1:
        print("{} is not a prime number!".format(num))
        return False
    for i in range(2, int(num/2 + 1)):
        if num % i == 0:
            print("{} is not a prime number!".format(num))
            return False
    print("{} is a prime number!".format(num))
    return True

main()