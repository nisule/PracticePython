def main():
    a = [5, 10, 15, 20, 25]
    print(getEnds(a))

def getEnds(myList):
    return [myList[0],  myList[len(myList)-1]] # returns a new list with the first and last element of the input list

main()