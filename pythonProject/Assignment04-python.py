
scores = [56, 70, 87, 90, 77, 92, 67, 82]
print("\nThese are the given scores:")
print(*scores, sep=', ')
length = len(scores)
print(f"\nNumber of scores: {length}")
scores.sort()
second = scores[-2]
print(f"\nThe runner-up score is: {second}")
