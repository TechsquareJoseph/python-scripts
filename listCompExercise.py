#create the two lists one of numbers and newlist, into which the positive numbers will go
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = []

for number in numbers:
    if number > 0:
        newlist.append(int(number))


print(newlist)
