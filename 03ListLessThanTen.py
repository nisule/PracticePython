myList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList = []
for num in myList:
    if (num < 5):
        newList.append(num)

print(newList)
newList2 = []
target = input("Please enter a number, list will return only elements smaller than the number you enter: ")
for num in myList:
    if (num < int(target)):
        newList2.append(num)

print(newList2)
