a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

newList = []

for x in range(0, len(a)):
    for y in range(0, len(b)):
        if (a[x] == b[y]):
            newList.append(a[x])

newList = list(set(newList)) # making it a set and turning it back into a list removes duplicates
print(newList)

