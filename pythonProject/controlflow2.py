print("please enter a number between 1 and 10: ")
guess = int(input())
if guess != 5:
    if guess < 5:
        print("Please guess higher")
    else:
        print("please guess lower")

    print("please enter your guess again: ")
    guess = int(input())
    if guess == 5:
        print("WELL DONE")
    else:
        print(" SORRY you didn't guess it")
else:
    print("you guess it the First time")
