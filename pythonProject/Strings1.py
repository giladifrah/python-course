#                   1
#         01234567890123
parrot = "Norwegian Blue"

print(parrot[0:6:2])
print(parrot[0:6:3])



number = "9,233;372:036 854,775;807"
seperators = number[1::4]
print(seperators)


values = "".join(char if char not in seperators else " " for char in number).split()
print(values)
print([int(val) for val in values])

for x in number:
    if x not in seperators:
        print(x)

print()


# .join() with lists
numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))