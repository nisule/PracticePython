import random as r

a = []
b = []

for i in range(0, r.randint(10, 21)):
    a.append(r.randint(0,21))
for i in range(0, r.randint(10, 21)):
    b.append(r.randint(0, 21))
print(a)
print(b)

c = [x for x in a for y in b if x == y]
c = list(set(c))

print(c)