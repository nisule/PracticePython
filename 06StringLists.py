s = input("Enter a string: ")

forwards = []
backwards = []

for ch in s:
    forwards.append(ch)

i = len(forwards)-1
while i >= 0:
    backwards.append(forwards[i])
    i -= 1
print(forwards)
print(backwards)

if forwards == backwards:
    print("{} is a palindrome!".format(s))
else:
    print("{} is not a palindrome!".format(s))