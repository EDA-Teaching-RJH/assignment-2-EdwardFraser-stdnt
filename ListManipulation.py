list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
list.sort()
sevenandeight = [7,8]
list.extend(sevenandeight)
for i in list:
    if 1 in list:
        list.remove(1)
    else:
        break
print(list)