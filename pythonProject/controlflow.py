name = input("Please enter name ")
age = int(input("How old are you, {0} ? ".format(name)))
print(age)

if age >= 18:
    print("You are old enough to vote ")
    print("Please put X in the box")
else:
    print("Come back in {0} years ".format(18-age))
