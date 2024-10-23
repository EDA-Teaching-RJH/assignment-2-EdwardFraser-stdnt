import random
c = []
i=0
while i < 10:
    c.append(random.randint(1,100))
    i+=1
newarr = []
for x in c:
    if x % 2 == 0:
        break
    elif x % 2 != 0:
        newarr.append(x)
    else:
        break
j=0
while j < len(c):
    if c[j] % 2 == 0:
        c.pop(j)
    else:
        j =j+1
print(c)