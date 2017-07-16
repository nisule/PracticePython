def main():
    print(fib())

def fib():
    num = int(input("Enter how many fibonacci numbers you want calculated : "))

    if num == 1: # kinda pointless if a really small number is entered so just return this
        return [1]
    if num == 2:
        return [1, 1]
    else: # where the real work happens
        list = [1, 1] # so the recursive function can do its thing
        fibRecur(num, list) # calls the recursive function
        return list

def fibRecur(num, list): # WHERE THE MAGIC HAPPENS, recursive function
    if num > 0: # base case, cuz the user entered how many numbers they wanted generated
       # print(list)
        num -= 1 # decrements the num so it doesnt go on forever
        list.append(list[len(list)-2] + list[len(list)-1]) # adds the last 2 numbers of the fib sequence and appends it to list
        return fibRecur(num, list) # calls itself with update num and list

main()