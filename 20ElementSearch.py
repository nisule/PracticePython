
def binarySearch(list, value):
    first = 0
    last = len(list) - 1
    mid = round((first + last) / 2)
    print(binarySearchRecursive(list, value, first, mid, last))

def binarySearchRecursive(list, value, first, mid, last):
    if value == list[mid]:
        return True
    elif mid < first:
        return False
    elif mid > last:
        return False
    elif value < list[mid]:
        last = mid-1
        mid = round((first + last)/2)
        return binarySearchRecursive(list, value, first, mid, last)
    elif value > list[mid]:
        first = mid + 1
        mid = round((first + last)/2)
        return binarySearchRecursive(list, value, first, mid, last)




myList = [1, 3, 5, 30, 42, 43, 500]
binarySearch(myList, 1)
binarySearch(myList, 2)
binarySearch(myList, 3)
binarySearch(myList, 5)
binarySearch(myList, 30)
binarySearch(myList, 42)
binarySearch(myList, 43)
binarySearch(myList, 500)
binarySearch(myList, -1)
binarySearch(myList, 0)
binarySearch(myList, 1000)


